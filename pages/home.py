import streamlit as st
import json
import requests
from streamlit_lottie import st_lottie
from pages import error

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    c1, c2 = st.columns((3,1))
    
    with c2:
        lottie_file = load_lottiefile("assets/schedule.json")  # replace link to local lottie file
        # lottie_file = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_ok9cq9zj.json")

        st_lottie(
            lottie_file,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # small; medium ; high
            renderer="svg", # svg; canvas
            height=None,
            width=None,
            key="lottie-schedule",
        )
    
    with c1:
        if 'start' not in st.session_state:
            st.session_state['start'] = False
        
        body = st.container()
        
        for i in range(2):
            body.write(' ')
        
        st.warning(st.session_state['start'])
        
        st.markdown("""
        <style>
        div.stButton > button {
            background-color: #f72585;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            width: 50%;
        }
        div.stButton > button:hover {
            background-color: #f8f8f8;
            box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 10px 20px 0 rgba(0,0,0,0.19);
        }
        </style>""", unsafe_allow_html=True)
        
        if st.button("Get Started") or st.session_state['start']:
            st.session_state['start'] = True
            body.success('Cieee udah ready nih')
        else:
            body.title("JAKA", 'get-started')
            about_text = """
                Jaka is built to make Universitas Indonesia students' course scheduling
                easier, faster, seamless, and more intuitive than ever.
            """
            body.write(about_text)
            for i in range(2):
                body.write(' ')
