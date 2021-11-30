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

def goto(page):
    st.session_state['menu'] = page

def app():
    st.markdown("<center><h1 style='text-align: center;'>What Do You Want To Do?</h1></center>", unsafe_allow_html=True)
    
    #st.info('Actions: '+str(st.session_state['actions']))
    c1, a1, c2, a2, c3 = st.columns((2, 1, 2, 1, 2))
    
    with c1:
        lottie_url = "https://assets10.lottiefiles.com/packages/lf20_zuiv9qn4.json"
        lottie_json = load_lottieurl(lottie_url)

        st_lottie(
            lottie_json,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # small; medium ; high
            renderer="svg", # svg; canvas
            height=None,
            width=None,
            key="lottie-create-schedule",
        )
        st.button("Create Schedule", on_click=goto('Create Schedule'))
        
    with c2:
        lottie_url = "https://assets5.lottiefiles.com/packages/lf20_7k4anl64.json"
        lottie_json = load_lottieurl(lottie_url)

        st_lottie(
            lottie_json,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # small; medium ; high
            renderer="svg", # svg; canvas
            height=None,
            width=None,
            key="lottie-modify-schedule",
        )
        st.button('Modify Schedule', on_click=goto('Modify Schedule'))
        
    with c3:
        lottie_url = "https://assets10.lottiefiles.com/packages/lf20_v6sxmrkx.json"
        lottie_json = load_lottieurl(lottie_url)

        st_lottie(
            lottie_json,
            speed=1,
            reverse=False,
            loop=True,
            quality="high", # small; medium ; high
            renderer="svg", # svg; canvas
            height=None,
            width=None,
            key="lottie-delete-schedule",
        )
        st.button('Delete Schedule', on_click=goto('Delete Schedule'))
