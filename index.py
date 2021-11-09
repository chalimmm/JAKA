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
    'Home'
    ,'Login'
    ,'Schedule'
    ,'Settings'
    # ,'View Plan'    
]
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
p {
font-family: 'Montserrat';font-size: 12px;
}
</style>""", unsafe_allow_html=True)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">
<style>
a {
font-family: 'Montserrat';font-size: 25px;
}
</style>""", unsafe_allow_html=True)

h1, empty, h2 = st.columns((1, 4, 1))

if 'start' not in st.session_state:
    st.session_state['start'] = False

with h1: # Kolom kiri untuk logo
    st.markdown('''
    <a href="#"><img src="https://i.ibb.co/yP2wjhW/jaka-02.png" alt="Logo JAKA" style="width:42px;height:42px;"></a>
    ''', unsafe_allow_html=True)
    st.write(" ")
    st.image(
        'https://i.ibb.co/yP2wjhW/jaka-02.png'
        ,width=75
    )
with h2: # Dropdown menu
    menu = st.selectbox(
        label='Go To',
        options=page_list,
    )

# st.sidebar.image('https://i.ibb.co/yP2wjhW/jaka-02.png', width=150)
# menu = st.sidebar.selectbox(label='Go To', options=page_list)

if menu == 'Home':
    if st.session_state['start']:
        login.app()
    else:
        home.app()
elif menu == 'Schedule':
    schedule.app()
elif menu == 'Login':
    login.app()
elif menu == 'Settings':
    settings.app()
else:
    error.app(307)
