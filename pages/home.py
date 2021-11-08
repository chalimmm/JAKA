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
    c1, c2 = st.columns(2)
    
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
        
        #st.warning(st.session_state['start'])
        
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
        
        st.markdown("""
        <link href='https://fonts.googleapis.com/css?family=Montserrat' rel='stylesheet'>
        <style>
        body {
        font-family: 'Montserrat';font-size: 22px;
        }
        </style>""", unsafe_allow_html=True)
        
        if st.button("Get Started") or st.session_state['start']:
            st.session_state['start'] = True
            body.success('Cieee udah ready nih')
        else:
            body.title("JAKA", 'get-started')
            body.write("Jadwal Aman, Kuliah Aman.")
            #body.markdown("""<hr size="4px" width="100%" color="#f72585">""", unsafe_allow_html=True)
            
            body.markdown("""
            <h1>Montserrat</h1>
            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit.</p>
            <p>123456790</p>
            <p>ABCDEFGHIJKLMNOPQRSTUVWXYZ</p>
            <p>abcdefghijklmnopqrstuvwxyz</p>
            <hr style="height:4px;border:none;color:#f72585;background-color:#f72585" /> """, unsafe_allow_html=True)
            
            about_text = """
                Jaka is built to make Universitas Indonesia student's course scheduling easier, faster, seamless, and more intuitive than ever.
            """
            body.header(about_text)
            for i in range(2):
                body.write(' ')
