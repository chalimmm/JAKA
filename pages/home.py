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
        
        if st.button("Get Started") or st.session_state['start']:
            st.session_state['start'] = True
            body.success('Cieee udah ready nih')
        else:
            body.title("JAKA", 'get-started')
            st.markdown("<h2>Jadwal Aman, Kuliah Aman.</h2>", unsafe_allow_html=True)
            #body.write("Jadwal Aman, Kuliah Aman.")
            #body.markdown("""<hr size="4px" width="100%" color="#f72585">""", unsafe_allow_html=True)
            
            body.markdown("""
            <hr style="height:4px;border:none;color:#f72585;background-color:#f72585" /> """, unsafe_allow_html=True)
            
            about_text = """
                JAKA is built to make Universitas Indonesia student's course scheduling easier, faster, seamless, and more intuitive than ever.
            """
            body.write(about_text)
            for i in range(2):
                body.write(' ')
