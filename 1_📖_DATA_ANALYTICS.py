import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(
    page_title="DATA ANALYTICS",
    page_icon="🙋‍♂️",
    initial_sidebar_state="auto",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .circular-image {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid #4f8bf9;
    }
    .header-container {
        display: flex;
        align-items: center;
        gap: 20px;
        margin-bottom: 30px;
    }
    .social-icon {
        width: 24px;
        height: 24px;
        vertical-align: middle;
        margin-right: 5px;
    }
    .intro-text {
        text-align: justify;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# Header Section
col1, col2 = st.columns([1, 4])
with col1:
    # Using a placeholder image (replace with your actual image URL)
    image_url = "https://placehold.co/150x150"
    st.markdown(f"""
    <div style="display: flex; justify-content: center;">
        <img src="{image_url}" class="circular-image">
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="margin-top: 10px;">
        <h2>Atul Bhardwaj</h2>
        <p style="color: #6c757d; margin-top: -10px;">Data Analyst | Full Stack Developer</p>
    </div>
    """, unsafe_allow_html=True)

# Main Content
st.title("Home")

# Social links with better formatting
st.markdown("""
### Connect With Me ⛓️‍💥
<div style="margin-bottom: 30px;">
    <a href="https://www.linkedin.com/in/atul-bhardwaj-40041a1aa" target="_blank" style="text-decoration: none;">
        <img src="https://cdn-icons-png.flaticon.com/24/174/174857.png" class="social-icon"> LinkedIn
    </a> &nbsp; | &nbsp;
    <a href="https://github.com/atul320" target="_blank" style="text-decoration: none;">
        <img src="https://cdn-icons-png.flaticon.com/24/733/733553.png" class="social-icon"> GitHub
    </a> &nbsp; | &nbsp;
    <a href="mailto:bhardwajatul320@gmail.com" style="text-decoration: none;">
        <img src="https://cdn-icons-png.flaticon.com/24/281/281764.png" class="social-icon"> Email
    </a>
</div>
""", unsafe_allow_html=True)

# Introduction section
st.markdown("""
### 🚀 About My Data Analytics Journey

<div class="intro-text">
I am Atul Bhardwaj, a dedicated and results-driven professional with a Master's degree in Computer Applications from Gautam Buddha University and a Bachelor's degree in Computer Applications from G.L Bajaj Institute of Technology & Management.

With a strong foundation in software development, data analytics, and front-end technologies, I have worked in dynamic environments like Kalkine Consultancy India Private Limited, where I contributed to optimizing web platforms and enhancing user experiences.

I am proficient in:
- **Programming**: Java, Python, JavaScript
- **Web Technologies**: React.js, Node.js
- **Databases**: MySQL, MongoDB
- **Data Tools**: FastAPI, Matplotlib, Streamlit

Here, I am learning by doing hands-on projects where I apply data analytics skills to track, compare, and visualize stock market trends. These projects enhance my analytical thinking and provide real-time insights into financial markets, further solidifying my skills in Python programming, data manipulation, and visualization tools.

With a keen interest in data analytics, software development, and a proactive learning approach, I aim to leverage my skills to contribute effectively in a challenging and growth-oriented role.
</div>

**ENJOY EXPLORING MY WORK!** ✨
""", unsafe_allow_html=True)

# Add some space at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
