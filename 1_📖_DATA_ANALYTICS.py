import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="DATA ANALYTICS",
    page_icon="🙋‍♂️",
    initial_sidebar_state="auto"
)

# Function to load image with persistent caching
@st.cache_data(ttl=3600)  # Cache for 1 hour
def load_image_from_drive():
    try:
        # Direct Google Drive image URL
        image_url = "https://drive.google.com/uc?export=view&id=12mFpRvjSkwVf85RdyZj1TBet6m-WlJop"
        response = requests.get(image_url, stream=True)
        response.raise_for_status()
        return Image.open(BytesIO(response.content))
    except:
        return None

# Load the image
profile_img = load_image_from_drive()

# CSS for circular image
circle_image_style = """
<style>
.circular-image-container {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    overflow: hidden;
    border: 2px solid #4f8bf9;
}
.circular-image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>
"""
st.markdown(circle_image_style, unsafe_allow_html=True)

# Display section
if profile_img:
    # Display using st.image() for reliability
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("""
        <div class="circular-image-container">
            <img src="https://drive.google.com/uc?export=view&id=12mFpRvjSkwVf85RdyZj1TBet6m-WlJop">
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("<h2>Atul Bhardwaj</h2>", unsafe_allow_html=True)
else:
    # Fallback that doesn't show placeholder
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 20px;">
        <h2>Atul Bhardwaj</h2>
    </div>
    """, unsafe_allow_html=True)

# Page title
st.title("Home")

# Social links and intro (maintaining your original bullet-point format)
st.markdown('''
### Connect ⛓️‍💥 and Follow!
* ![Linkedin](https://cdn-icons-png.flaticon.com/24/174/174857.png) &nbsp; [LinkedIn](https://www.linkedin.com/in/atul-bhardwaj-40041a1aa)
* ![GitHub](https://cdn-icons-png.flaticon.com/24/733/733553.png) &nbsp; [GitHub](https://github.com/atul320)
* ![Gmail](https://cdn-icons-png.flaticon.com/24/281/281764.png) &nbsp; [Gmail](mailto:bhardwajatul320@gmail.com)

### Hi, This is My Python Streamlit and Data Analytics Learning Playground

I am Atul Bhardwaj, a dedicated and results-driven professional with a Master's degree in Computer Applications from Gautam Buddha University and a Bachelor's degree in Computer Applications from G.L Bajaj Institute of Technology & Management.

With a strong foundation in software development, data analytics, and front-end technologies, I have worked in dynamic environments like Kalkine Consultancy India Private Limited, where I contributed to optimizing web platforms and enhancing user experiences.

I am proficient in:
- **Programming**: Java, Python, JavaScript
- **Web Technologies**: React.js, Node.js
- **Databases**: MySQL, MongoDB
- **Data Tools**: FastAPI, Matplotlib, Streamlit

Here, I am learning by doing hands-on projects where I apply data analytics skills to track, compare, and visualize stock market trends. These projects enhance my analytical thinking and provide real-time insights into financial markets, further solidifying my skills in Python programming, data manipulation, and visualization tools.

In addition to my technical expertise, I am well-versed in Agile environments and continuously strive to improve my knowledge through various internships, courses, and certifications.

With a keen interest in data analytics, software development, and a proactive learning approach, I aim to leverage my skills to contribute effectively in a challenging and growth-oriented role.

**ENJOY!!!**
''', unsafe_allow_html=True)
