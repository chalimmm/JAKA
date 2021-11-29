import streamlit as st
import subprocess
### FIRESTORE SECTION ###
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("pages/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

def authFirebase(u, p):
    with st.spinner('Authenticating...'):
        subprocess.call(["python", "pages/scraping.py", u, p])

    db = firestore.client()

    users = db.collection('users').document(u).get()
    
    if users.exists and st.session_state['isAgree']:
        st.session_state['username'] = u
        st.session_state['logged_in'] = True
        st.success('You are authorized.')
        st.success('Logging in to JAKA')
        st.session_state['menu'] = 'Setting'
    else:
        st.warning('Sorry, you are not authorized.')
        st.warning('Wrong username or password.')        
        
def app():
    st.markdown("<h1 style='text-align: center;'>JAKA</h1>", unsafe_allow_html=True)
    st.markdown("<center><a style='text-align: center;'>Sign in to your SSO-UI account.</a></center>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    
    left, center, right = st.columns([1, 2, 1])
    with center:
        with st.form('loginForm'):
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
            submitted = st.form_submit_button("Login")
            if submitted:
                authFirebase(u, p)
        
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
