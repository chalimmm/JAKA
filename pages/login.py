import streamlit as st
import pyrebase
import hashlib
import subprocess

def authFirebase(u, p):
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
        passwd = hashlib.sha256(p.encode('utf-8')).hexdigest()
        try:
            user = auth.create_user_with_email_and_password(email, passwd)
            data = {
                email: {
                    "username": u
                }
            }
            
            db.child("users").push(data, user['idToken'])
        except:
            pass
        try:
            user = auth.sign_in_with_email_and_password(email, passwd)
            # st.success('Welcome ' + u)
            st.session_state['logged_in'] = st.session_state['isAgree']
            with st.spinner('Authenticating...'):
                subprocess.call(["python", "pages/scraping.py", u, p])
            st.session_state['menu'] = 'Settings'
            st.session_state['temp'] = 1
            st.success('Authenticated')
        except:
            st.warning('Authentication Failed')        
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
            st.subheader("""
                Dengan menggunakan JAKA, Anda setuju dengan Kebijakan Privasi kami, yaitu:\n
                1. JAKA menggunakan informasi login berupa username dan kata sandi akun Single-Sign-On Universitas Indonesia untuk masuk ke SIAK-NG.\n
                2. Informasi login tersebut digunakan untuk proses otentikasi, yaitu untuk memastikan bahwa pihak yang sedang melakukan proses tersebut adalah mahasiswa aktif di Universitas Indonesia.\n
                3. Selain untuk proses otentikasi, informasi login tersebut juga digunakan untuk proses pengambilan data dari halaman jadwal yang ada pada SIAK-NG untuk dapat diproses pada situs web JAKA agar mahasiswa dapat menyusun beberapa jadwal dari data yang sudah diambil.\n
                4. JAKA TIDAK menyimpan informasi login mahasiswa dalam bentuk apapun.\n
                5. Perlu diingat bahwa JAKA tidak bertanggung jawab apabila mahasiswa tidak dapat mengambil jadwal sesuai dengan apa yang direkomendasikan oleh JAKA.\n
                6. Perlu diingat bahwa pengguna JAKA harus mempertimbangkan jumlah SKS maksimum yang dapat diambil pada setiap penyusunan jadwal, karena JAKA menyamaratakan jumlah SKS maksimum untuk setiap mahasiswa, yaitu 24 SKS.\n
            """)
        st.session_state['isAgree'] = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
        st.button('Login', on_click=authFirebase(u, p))
        
def reset():
    for key in st.session_state.keys():
        del st.session_state[key]

def out():
    st.markdown("<h1 style='text-align: center;'>JAKA</h1>", unsafe_allow_html=True)
    st.markdown("<center><a style='text-align: center;'>Sign in to your SSO-UI account.</a></center>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown("<center><a style='text-align: center;'>Yakin mau keluar?</a></center>", unsafe_allow_html=True)
        st.button('Iya, yakin.', on_click=reset())
