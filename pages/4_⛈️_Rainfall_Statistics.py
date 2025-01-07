import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="RAINFALL STATISTICS",
    page_icon="⛈️",
    initial_sidebar_state="auto"
)

st.markdown('''
# Rainfall Statistics and Analysis in India from 1901 to 2017
This app retrieves rainfall data from **CSV FILE** and displays tables and so statistics taken from **[Rainfall data from government site](https://www.data.gov.in/catalog/rainfall-india)**.

### **Python Libraries Used:**
- `streamlit`
- `pandas`

### **Data Source:**
* [Github File you can check](https://en.wikipedia.org/wiki/NIFTY_500) or you can download from [Rainfall data from government site](https://www.data.gov.in/catalog/rainfall-india)
''')

def load_data(file):
    df = pd.read_csv(file)
    return df

def calculate_combined_average_and_change(df):
    month_columns = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
    df['COMBINED_AVERAGE'] = df[month_columns].mean(axis=1)
    df_sorted = df.sort_values(by=["SUBDIVISION", "YEAR"])
    df_sorted['PERCENTAGE_CHANGE'] = df_sorted.groupby('SUBDIVISION')['ANNUAL'].pct_change() * 100
    return df_sorted

def plot_combined_average(df):
    subdivision_avg = df.groupby('SUBDIVISION')['COMBINED_AVERAGE'].mean().sort_values(ascending=False)
    st.bar_chart(subdivision_avg)

def plot_rainfall(df, selected_subdivision):
    subdivision_data = df[df['SUBDIVISION'] == selected_subdivision]
    st.line_chart(subdivision_data.set_index('YEAR')['ANNUAL'])

st.title("Sub Divisional Monthly Rainfall Data")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file is not None:
    df = load_data(uploaded_file)
    df = calculate_combined_average_and_change(df)
    st.write("### Combined Average Rainfall by Sub-Division")
    st.dataframe(df)
    selected_year = st.sidebar.selectbox("Select Year", df['YEAR'].unique())
    selected_subdivision = st.sidebar.selectbox("Select Sub-Division", df['SUBDIVISION'].unique())
    subdivision_data = df[(df['SUBDIVISION'] == selected_subdivision) & (df['YEAR'] == selected_year)]
    if not subdivision_data.empty:
        percentage_change = subdivision_data['PERCENTAGE_CHANGE'].values[0]
        if pd.notnull(percentage_change):
            st.sidebar.write(f"Percentage Change in Rainfall for {selected_subdivision} in {selected_year}: {percentage_change:.2f}%")
        else:
            st.sidebar.write(f"Data for {selected_subdivision} in {selected_year} is missing or the first year in data.")
    plot_combined_average(df)
    plot_rainfall(df, selected_subdivision)
