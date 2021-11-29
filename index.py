import streamlit as st
from pages import home, login, error, schedule, settings

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
page_list = [
    'Schedule'
    ,'Settings'
    ,'Logout'
    # ,'View Plan'    
]
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

if 'isLogin' not in st.session_state:
    st.session_state['isLogin'] = False
    
if 'isAgree' not in st.session_state:
    st.session_state['isLogin'] = False

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if 'actions' not in st.session_state:
    st.session_state['actions'] = 1

if 'username' not in st.session_state:
    st.session_state['username'] = 'username'

# def menuCallback():
#     st.session_state['menu'] = st.session_state['page']

logo, empty, menu = st.columns((1, 3, 1))

with logo: # Kolom kiri untuk logo
    st.markdown('''
    <a href="javascript:location.reload(true)">
    <img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:50px;height:50px;">
    </a>
    ''', unsafe_allow_html=True)
with menu: # Dropdown menu
    navBar = st.container()
    if st.session_state['logged_in']:
        st.session_state['menu']=navBar.selectbox(label='Go To',options=page_list,index=st.session_state['actions'])

if st.session_state['menu'] == 'Home':
    home.app()
elif st.session_state['menu'] == 'Schedule':
    st.session_state['actions'] = 0
    if schedule.app():
       schedule.SelectSchedule()
elif st.session_state['menu'] == 'Login':
    login.app()
elif st.session_state['menu'] == 'Logout':
    login.out()
elif st.session_state['menu'] == 'Settings':
    st.session_state['actions'] = 1
    settings.app()
else:
    error.app(307)
