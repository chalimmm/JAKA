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
    c1, c2, c3 = st.columns(3)
    
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
            key="lottie-schedule",
        )
        is_create = st.form_submit_button('Create Schedule')
        
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
            key="lottie-schedule",
        )
        is_modify = st.form_submit_button('Modify Schedule')
        
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
            key="lottie-schedule",
        )
        is_delete = st.form_submit_button('Delete Schedule')
