### IMPORT LIBRARIES AND PAGES ###
import streamlit as st
from pages import home, login, error, schedule, dashboard

### INIT SESSION STATE ###
if 'menu'           not in st.session_state : st.session_state['menu']           = 'Home'
if 'auth'           not in st.session_state : st.session_state['auth']           = False
if 'courses'        not in st.session_state : st.session_state['courses']        = {}
if 'username'       not in st.session_state : st.session_state['username']       = 'username'
if 'selectedCourse' not in st.session_state : st.session_state['selectedCourse'] = []

### PAGE STYLING ###
st.set_page_config(
        page_title = "JAKA",
        layout = "wide",
        page_icon = "https://i.ibb.co/yP2wjhW/jaka-02.png",
        initial_sidebar_state = "collapsed"
    )
css_style = """
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap" rel="stylesheet">
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
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
        div.customButton > button {
            background-color: #3a0ca3;
            border-radius: 50px;
            display: inline-block;
            border: none;
            transition: all 0.4s ease 0s;
            color: #ffffff;
            padding: 15px 32px;
            text-align: center;
            text-transform: uppercase;
            text-decoration: none;
            display: inline-block;
            font-family: 'Montserrat';
            font-weight: 700;
            margin: 4px 2px;
            width: 100%;
        }
        div.customButton > button:hover {
            background-color: #f8f8f8;
            color: #3a0ca3;
            box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 10px 20px 0 rgba(0,0,0,0.19);
        }
        h1 { font-family: 'Montserrat';font-size: 55px; font-weight: 900; }
        h2,h3,h4,h5 { font-family: 'Montserrat'; }
        p.judul { font-family: 'Montserrat'; font-size: 35px; font-weight: 710; }
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

### CALLBACK FUNCTION ###
def goto(page):
    st.session_state['menu'] = page

### HEADER SECTION ###
st.sidebar.write(" ")
st.sidebar.write(" ")
logoSide, titleSide = st.sidebar.columns([1, 2])
logoSide.markdown('''
    <center>
    <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    </center>
    ''', unsafe_allow_html=True)
titleSide.markdown("""
    <p class='judul' align='center'>
        <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
            JAKA UI 
        </a>
    </p>
    """, unsafe_allow_html=True)
logoMain, textMain = st.columns((1, 5))
if st.session_state['auth'] and st.session_state['menu'] != 'Login':
    logoMain.markdown('''
    <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[1].click();">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    ''', unsafe_allow_html=True)
    textMain.markdown("""
    <h4 align='right'>
        <a href="javascript:document.getElementsByClassName('css-1ydp377 edgvbvh6')[2].click();">
            Hai, """+st.session_state['username']+""" 
        </a>
    </h4>
    """, unsafe_allow_html=True)
    st.sidebar.button('Dashboard', on_click=goto, args=['Dashboard'])
    st.sidebar.markdown("""
    <a href='javascript:if(confirm("Are you sure to logout?")) window.location.reload(true);'>
        <div class="customButton">
            <button>
                Logout
            </button>
        </div>
    </a>
    """, unsafe_allow_html=True)
elif st.session_state['menu'] == 'Home':
    logoMain.markdown('''
    <a href="javascript:window.location.reload(true);">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    ''', unsafe_allow_html=True)
    textMain.markdown("""
    <h4 align='right'>
        <a href="javascript:document.getElementsByClassName('css-1wwkvaf edgvbvh1')[0].click();">
            Login 
        </a>
    </h4>
    """, unsafe_allow_html=True)
else:
    logoMain.markdown('''
    <a href="javascript:window.location.reload(true);">
        <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;"/>
    </a>
    ''', unsafe_allow_html=True)

### PAGE CONTROLLER ###
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
    else:
        dashboard.app()
else:
    if st.session_state['menu'] == 'Home':
        home.app()
    elif st.session_state['menu'] == 'Login':
        login.app()
    else:
        error.app(307)