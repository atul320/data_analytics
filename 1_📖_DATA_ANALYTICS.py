import streamlit as st

# Page configuration
st.set_page_config(
    page_title="DATA ANALYTICS",
    page_icon="🙋‍♂️",
    initial_sidebar_state="auto"
)

# Define image URL (from Google Drive direct view link)
image_url = "https://drive.google.com/uc?export=view&id=12mFpRvjSkwVf85RdyZj1TBet6m-WlJop"

# CSS for circular image
circle_image_style = """
<style>
.circular-image {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    object-fit: cover;
}
</style>
"""

# Inject CSS
st.markdown(circle_image_style, unsafe_allow_html=True)

# Display image and name in a row
st.markdown(f"""
<div style="display: flex; align-items: center; gap: 10px;">
    <img src="{image_url}" class="circular-image">
    <h2>Atul Bhardwaj</h2>
</div>
""", unsafe_allow_html=True)

# Page title
st.title("Home")

# Social links and intro
st.markdown('''
### Connect ⛓️‍💥 and Follow!
* ![Linkedin](https://cdn-icons-png.flaticon.com/24/174/174857.png) &nbsp; [LinkedIn](https://www.linkedin.com/in/atul-bhardwaj-40041a1aa)
* ![GitHub](https://cdn-icons-png.flaticon.com/24/733/733553.png) &nbsp; [GitHub](https://github.com/atul320)
* ![Gmail](https://cdn-icons-png.flaticon.com/24/281/281764.png) &nbsp; [Gmail](mailto:bhardwajatul320@gmail.com)

### Hi, This is My Python Streamlit and Data Analytics Learning Playground

I am Atul Bhardwaj, a dedicated and results-driven professional with a Master's degree in Computer Applications from Gautam Buddha University and a Bachelor's degree in Computer Applications from G.L Bajaj Institute of Technology & Management.

With a strong foundation in software development, data analytics, and front-end technologies, I have worked in dynamic environments like Kalkine Consultancy India Private Limited, where I contributed to optimizing web platforms and enhancing user experiences.

I am proficient in Java, Python, JavaScript, React.js, Node.js, MySQL, and other related technologies.

Here, I am learning by doing hands-on projects where I apply data analytics skills to track, compare, and visualize stock market trends. These projects enhance my analytical thinking and provide real-time insights into financial markets, further solidifying my skills in Python programming, data manipulation, and visualization tools.

In addition to my technical expertise, I am well-versed in Agile environments and continuously strive to improve my knowledge through various internships, courses, and certifications.

With a keen interest in data analytics, software development, and a proactive learning approach, I aim to leverage my skills to contribute effectively in a challenging and growth-oriented role.

**ENJOY!!!**
''', unsafe_allow_html=True)
