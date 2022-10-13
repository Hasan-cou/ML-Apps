import streamlit as st
from mp import MP
from forms import dl, intelli, du, dv, evaluation

# create page title
st.set_page_config(
    layout="wide",
    page_title="Machine Learning",
    page_icon="👨‍💻",
)
# instance of our system
ml = MP()

# Hide streamlit default Logo
hide_streamlit_style = """ 
 <style>
     #MainMenu {visibility:hidden}
     footer{visibility:hidden}
    </style>
"""
# Remove Streamlit footer note and repository notes
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: center; color: black;'>Intelligent Web-based User Interface for Machine Learning Applications</h3>",
    unsafe_allow_html=True)

# Tab options to control other pages
# Not implemented yet
upload, analyze, learning, visualization, explanation = st.tabs(
    ["📨 Upload", "✅ Metadata", "⚙️Machine Learning", "📊Visualize", "📉Explanation"])

# Add all my application pages here
ml.connect("📨 Upload Data", dl.main)
ml.connect("✅ Change Metadata", du.main)
ml.connect("⚙️ Linear Regression", intelli.main)
ml.connect("📊 Data Analysis", dv.main)
ml.connect("📉 Optimization and Evaluation", evaluation.main)

# The main app
ml.start()
