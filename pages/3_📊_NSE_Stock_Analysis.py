import pandas as pd
import streamlit as st
from bs4 import BeautifulSoup
import io
import base64
import requests
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="NSE STOCK ANALYTICS",
    page_icon="📊",
    initial_sidebar_state="auto"
)

st.markdown('''
# NSE Stock Dashboard
This app retrieves stock prices from **Google** and displays tables from **Wikipedia**.

### **Python Libraries Used:**
- `streamlit`
- `pandas`
- `requests`
- `beautifulsoup`
- `matplotlib`

### **Data Source:**
* [Wikipedia](https://en.wikipedia.org/wiki/NIFTY_500)
''')

@st.cache_data
def load_data():
    url = 'https://en.wikipedia.org/wiki/NIFTY_500'
    html = pd.read_html(url, header=0)
    df = html[2]
    return df

st.header('NIFTY 500 Data from Wikipedia')
df = load_data()
st.dataframe(df, hide_index=True)
st.write("## Data Figures of Selected Organisations")

@st.cache_data
def load_stock(symbol):
    try:
        url = f'https://www.google.com/finance/quote/{symbol}:NSE'
        response = requests.get(url)
        if response.status_code != 200:
            return {'Symbol': symbol, 'Error': 'Failed to retrieve data'}
        soup = BeautifulSoup(response.text, 'html.parser')
        price = soup.find('div', {'class': 'YMlKec fxKbKc'})
        price = price.text if price else 'Data not available'
        metrics = soup.find_all('div', {'class': 'P6K39c'})
        data_dict = {
            'Symbol': symbol,
            'Price': price,
            'Previous Close': metrics[0].text if len(metrics) > 0 else 'Data not available',
            'Day Range': metrics[1].text if len(metrics) > 1 else 'Data not available',
            'Year Range': metrics[2].text if len(metrics) > 2 else 'Data not available',
            'Market Cap': metrics[3].text if len(metrics) > 3 else 'Data not available',
            'Avg Volume': metrics[4].text if len(metrics) > 4 else 'Data not available',
            'P/E Ratio': metrics[5].text if len(metrics) > 5 else 'Data not available',
            'Dividend Yield': metrics[6].text if len(metrics) > 6 else 'Data not available'
        }
        return data_dict
    except Exception as e:
        return {'Symbol': symbol, 'Error': str(e)}

selected_symbols = st.sidebar.multiselect(
    'Select symbols to display:',
    options=df['Symbol'],
    default=df['Symbol'][:3]
)

if selected_symbols:
    stock_data = [load_stock(symbol) for symbol in selected_symbols]
    final_data = pd.DataFrame(stock_data)
    st.dataframe(final_data, use_container_width=True, hide_index=True)

    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
        href = f'<a href="data:file/csv;base64,{b64}" download="NSE500.csv">Download CSV File</a>'
        return href

    st.markdown(filedownload(final_data), unsafe_allow_html=True)
    
    def parse_pe_ratio(pe_ratio):
        try:
            pe_ratio = pe_ratio.replace(',', '')
            return float(pe_ratio) if pe_ratio != 'Data not available' else None
        except ValueError:
            return None

    final_data['P/E Ratio'] = final_data['P/E Ratio'].apply(parse_pe_ratio)
    final_data = final_data.dropna(subset=['P/E Ratio'])

    fig, ax = plt.subplots()
    ax.bar(final_data['Symbol'], final_data['P/E Ratio'], color='skyblue')
    ax.set_xlabel('Stock Symbols')
    ax.set_ylabel('P/E Ratio')
    ax.set_title('P/E Ratio of Selected Symbols')
    ax.set_xticklabels(final_data['Symbol'], rotation=90, ha='right')
    chart_data = final_data[['Symbol', 'P/E Ratio']].set_index('Symbol')
    st.write("## P/E ratio, Price to the company's earnings per share of different Companies")
    newChart=st.bar_chart(chart_data)
else:
    st.write("No symbols selected. Please select at least one symbol.")
