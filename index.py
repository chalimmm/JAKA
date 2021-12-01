from requests.sessions import session
import streamlit as st
from pages import home, login, error, schedule, dashboard

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

st.set_page_config(
    page_title="JAKA",
    layout="wide",
    page_icon="https://i.ibb.co/yP2wjhW/jaka-02.png",
    initial_sidebar_state = "collapsed"
)

hide_menu_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

css_style = """
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
    h1 { font-family: 'Montserrat';font-size: 55px; font-weight: 900; }
    h2,h3,h4,h5 { font-family: 'Montserrat'; }
    p.info { font-family: 'Montserrat'; font-size: 25px; }
    p { font-family: 'Montserrat'; font-size: 16px; }
    a:link { font-family: 'Montserrat'; color: #3a0ca3; text-decoration:none; }
    a:hover { color: #f72585; text-decoration:none; }
    img:hover { opacity: 0.5; }
    label { font-family: 'Montserrat';font-size: 20px; font-weight: 600; }
    div.streamlit-expanderHeader { font-family: 'Montserrat';font-size: 20px; font-weight: 600; background-color: #f72585; color: #ffffff; }
    div.streamlit-expanderHeader:hover { background-color: #ffffff; color: #f72585; }
    div.streamlit-expanderContent { font-family: 'Montserrat'; font-size: 20px; }
    </style>
"""

st.markdown(css_style, unsafe_allow_html=True)

logoSide, titleSide = st.sidebar.columns((1, 3))
logoSide.markdown('''
    <center>
    <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    </center>
    ''', unsafe_allow_html=True)

def goto(page):
    st.session_state['menu'] = page

if st.session_state['auth']:
    logo, hai = st.columns((1, 5))
    hai.markdown("""
    <h4 align='right'>
        <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
            Hai, """+st.session_state['username']+""" 
        </a>
    </h4>
    """, unsafe_allow_html=True)
    titleSide.markdown("""
    <h2 align='left'>
        <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
            Hai, """+st.session_state['username']+""" 
        </a>
    </h2>
    """, unsafe_allow_html=True)
    st.sidebar.button('Logout', on_click=goto, args=['Logout'])
else:
    logo, empty, menu = st.columns((1, 4, 1))
    menu.subheader(st.session_state['menu'])
    titleSide.markdown("""
    <h2 align='left'>
        <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
            JAKA UI 
        </a>
    </h2>
    """, unsafe_allow_html=True)

with logo:
    st.markdown('''
    <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[1].click();">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    ''', unsafe_allow_html=True)

if st.session_state['auth']:
    if st.session_state['menu'] == 'Dashboard':
        dashboard.app()
    elif st.session_state['menu'] == 'Create Schedule':
        schedule.Course()
    elif st.session_state['menu'] == 'Modify Schedule':
        schedule.Course()
    elif st.session_state['menu'] == 'Delete Schedule':
        schedule.Course()
    elif st.session_state['menu'] == 'Choose Schedule':
        schedule.Class()
    elif st.session_state['menu'] == 'Logout':
        login.out()
    else:
        login.app()
else:
    if st.session_state['menu'] == 'Home':
        home.app()
    elif st.session_state['menu'] == 'Login':
        login.app()
    else:
        error.app(307)