import streamlit as st
import pyrebase
import hashlib

def auth(u, p):
    # Configuration Key
    firebaseConfig = {
        'apiKey': "AIzaSyA-QKAvK7mW2P_Fvzmd__m2jrEXDb2Yg3M",
        'authDomain': "jaka-id.firebaseapp.com",
        'projectId': "jaka-id",
        'databaseURL': "https://db-iaicg-default-rtdb.europe-west1.firebasedatabase.app",
        'projectId': "db-iaicg",
        'storageBucket': "jaka-id.appspot.com",
        'messagingSenderId': "1028592956608",
        'appId': "1:1028592956608:web:4449ccd5451f20b1946925",
        'measurementId': "G-CG71PW8JT8"
    }

    # Firebase Authentication
    firebase = pyrebase.initialize_app(firebaseConfig)
    auth = firebase.auth()

    # Database
    db = firebase.database()
    
    if st.session_state['isAgree']:
        email = u + '@ui.ac.id'
        passwd = hashlib.sha3_256(p.encode('utf-8')).hexdigest()
        try:
            user = auth.create_user_with_email_and_password(email, passwd)
            data = {
                "username": u
            }
            db.child("users").push(data, user['idToken'])
        except:
            # st.error('EMAIL EXIST!')
            pass
        try:
            user = auth.sign_in_with_email_and_password(email, passwd)
            st.session_state['logged_in'] = st.session_state['isAgree']
        except:
            # st.error('INVALID USERNAME OR PASSWORD!')
            pass
        
def app():
    st.markdown("<h1 style='text-align: center;'>JAKA</h1>", unsafe_allow_html=True)
    st.markdown("<center><a style='text-align: center;'>Sign in to your SSO-UI account.</a></center>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    
    left, center, right = st.columns([1, 2, 1])
    with center:
        u = st.text_input('Username', max_chars=30)
        p = st.text_input('Password', type='password', max_chars=30)
        with st.expander("Kebijakan Privasi JAKA"):
            st.write("""
                The chart above shows some numbers I picked for you.
                I rolled actual dice for these, so they're *guaranteed* to
                be random.
            """)
        st.session_state['isAgree'] = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
        st.button('Login', on_click=auth(u, p))
        
def reset():
    for key in st.session_state.keys():
        del st.session_state[key]

def out():
#     st.markdown("<h1 style='text-align: center;'>JAKA</h1>", unsafe_allow_html=True)
#     st.markdown("<center><a style='text-align: center;'>Sign in to your SSO-UI account.</a></center>", unsafe_allow_html=True)
#     st.write(" ")
#     st.write(" ")
    
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown("<center><a style='text-align: center;'>Yakin mau keluar?</a></center>", unsafe_allow_html=True)
        st.button('Iya, yakin.', on_click=reset())
