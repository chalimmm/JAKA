from requests.sessions import session
import streamlit as st
from pages import home, login, error, schedule, dashboard

st.set_page_config(
    page_title="JAKA",
    layout="wide"
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""

st.markdown(hide_menu_style, unsafe_allow_html=True)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap" rel="stylesheet">
<style>
div.stButton > button {
    background-color: #f72585;
    border-radius: 50px;
	display: inline-block;
	border: none;
	transition: all 0.4s ease 0s;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-transform: uppercase;
    text-decoration: none;
    display: inline-block;
    font-family: 'Montserrat';
    font-weight: 700;
    margin: 4px 2px;
    cursor: pointer;
    width: 100%;
}
div.stButton > button:hover {
    background-color: #f8f8f8;
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 10px 20px 0 rgba(0,0,0,0.19);
}
</style>""", unsafe_allow_html=True)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap" rel="stylesheet">
<style>
h1 {
font-family: 'Montserrat';font-size: 55px;
font-weight: 900;   
}
</style>""", unsafe_allow_html=True)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
<style>
p { font-family: 'Montserrat';font-size: 12px; }
a { font-family: 'Montserrat';font-size: 25px; }
</style>""", unsafe_allow_html=True) 

# Init Session State

if 'menu' not in st.session_state:
    st.session_state['menu'] = 'Home'

if 'auth' not in st.session_state:
    st.session_state['auth'] = False
    
if 'courses' not in st.session_state:
    st.session_state['courses'] = {}

if 'username' not in st.session_state:
    st.session_state['username'] = 'username'

if 'selectedCourse' not in st.session_state:
    st.session_state['selectedCourse'] = []

logo, empty, menu = st.columns((1, 3, 1))

with logo: # Kolom kiri untuk logo
    st.markdown('''
    <a href="javascript:location.reload(true)">
    <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;">
    </a>
    ''', unsafe_allow_html=True)

# st.info(st.session_state['auth'])
# st.info(st.session_state['menu'])

if st.session_state['auth']:
    if st.session_state['menu'] == 'Dashboard':
        dashboard.app()
    elif st.session_state['menu'] == 'Create Schedule':
        schedule.FilterCourse()
    elif st.session_state['menu'] == 'Modify Schedule':
        schedule.FilterCourse()
    elif st.session_state['menu'] == 'Delete Schedule':
        schedule.FilterCourse()
    elif st.session_state['menu'] == 'Choose Schedule':
        schedule.ChooseSchedule()
    elif st.session_state['menu'] == 'Logout':
        login.out()
    else:
        error.app(307)
else:
    if st.session_state['menu'] == 'Home':
        home.app()
    elif st.session_state['menu'] == 'Login':
        login.app()
    else:
        error.app(307)