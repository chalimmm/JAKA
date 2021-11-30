import streamlit as st
from pages import scraping

def goto(page):
    st.session_state['menu'] = page

def app():
    st.markdown("""
    <h1 style='text-align: center;'>
        JAKA
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <center>
        <a style='text-align: center;'>
            Login using your SSO-UI account.
        </a>
    </center>
    <br>
    <br>
    """, unsafe_allow_html=True)

    empty, center, empty = st.columns([1, 2, 1])
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
        isAgree = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
        
        status = st.container()
        
        if isAgree and not st.session_state['auth']:
            try:
                st.session_state['auth'] = scraping.app(u, p)
                if st.session_state['auth']:
                    status.success('Authenticated')
                else:
                    status.error('Wrong username or password')
            except:
                status.error('Wrong username or password')
                pass
        
        if st.session_state['auth'] and isAgree:
            st.button('Login', on_click=goto('Dashboard'))
        else:
            st.markdown("""
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap" rel="stylesheet">
            <style>
            div.disabledButton > button {
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
                cursor: not-allowed;
                width: 100%;
            }
            </style>""", unsafe_allow_html=True)
            st.markdown('''
                <div class='disabledButton'>
                <button disabled>
                Login
                </button>
                </div>
            ''', unsafe_allow_html=True)
        
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
