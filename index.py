import streamlit as st
from pages import home, login, error, schedule

st.set_page_config(
    page_title="JAKA",
    page_icon="random",
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
    # ,'View Plan'    
]

# st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# st.markdown("""
# <ul class="nav nav-tabs">
#   <li class="nav-item">
#     <a class="nav-link active" href="#">Home</a>
#   </li>
#   <li class="nav-item">
#     <a class="nav-link" href="#">Login</a>
#   </li>
#   <li class="nav-item">
#     <a class="nav-link" href="#">Schedule</a>
#   </li>
#   <li class="nav-item">
#     <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
#   </li>
# </ul>
# """, unsafe_allow_html=True)

h1, empty, h2 = st.columns((1, 4, 1))

with h1: # Kolom kiri untuk logo
    st.write(" ")
    st.write(" ")
    st.image(
        'https://i.ibb.co/yP2wjhW/jaka-02.png',
        width=80
    )

with h2: # Dropdown menu
    menu = st.selectbox(
        label='Go To',
        options=page_list,
    )

if menu == 'Home':
    home.app()
elif menu == 'Schedule':
    schedule.app()
else:
    error.app(307)
