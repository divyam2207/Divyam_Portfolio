import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide")

coder = "https://lottie.host/58295df6-a392-499d-a04c-4a576f5e8b4a/NawIQdtq2F.json"

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



st.write("##")
st.subheader("Hey guys :wave:")
st.title("My portfolio website..")
st.write("""
         This is a test writtent 
         """)
st.write("[Linkedin](https://www.linkedin.com/in/divyam2207)")
st.write("---")

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ["About", "Expreience", "Projects"],
        icons = ['person', 'code-slash','code-slash'],
        orientation="horizontal"
    )


if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Divyam Dubey")
            st.title("Graduate Student at University of Florida")
        with col2:
            st.lottie(load_lottie_url(coder))

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader(""" 
            Education
            - Master in Computer Science
           l             - University of Florida
                        - August 2024 - May 2026
            - Bachelors in Technology in Computer Science
                        - University of Technology of Madhya Pradesh
                        - August 2018 - May 2022
                        - Grade: 3.77/4        
            """)
            with col4:
                st.subheader(""" Testing """)