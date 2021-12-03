import streamlit as st
from pages import scraping

def goto(page):
    st.session_state['menu'] = page

def relogin():
    st.session_state['auth'] = False

def app():
    st.markdown("""
    <h1 style='text-align: center;'>
        JAKA
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <center>
        <p style='text-align: center;'>
            Login using your SSO-UI account.
        </p>
    </center>
    <br>
    <br>
    """, unsafe_allow_html=True)

    empty, center, empty = st.columns([1, 2, 1])
    with center:
        status = st.container()
        
        u = st.text_input('Username', help='Masukkan username akun SSO UI', max_chars=30)
        p = st.text_input('Password', help='Masukkan password akun SSO UI', type='password')
        with st.expander("Kebijakan Privasi JAKA"):
            st.write("""
                #### **Dengan menggunakan JAKA, Anda setuju dengan Kebijakan Privasi kami, yaitu:**\n
                1. JAKA menggunakan informasi login berupa username dan kata sandi akun Single-Sign-On Universitas Indonesia untuk masuk ke SIAK-NG.\n
                2. Informasi login tersebut digunakan untuk proses otentikasi, yaitu untuk memastikan bahwa pihak yang sedang melakukan proses tersebut adalah mahasiswa aktif di Universitas Indonesia.\n
                3. Selain untuk proses otentikasi, informasi login tersebut juga digunakan untuk proses pengambilan data dari halaman jadwal yang ada pada SIAK-NG untuk dapat diproses pada situs web JAKA agar mahasiswa dapat menyusun beberapa jadwal dari data yang sudah diambil.\n
                4. JAKA TIDAK menyimpan informasi login mahasiswa dalam bentuk apapun.\n
                5. Perlu diingat bahwa JAKA tidak bertanggung jawab apabila mahasiswa tidak dapat mengambil jadwal sesuai dengan apa yang direkomendasikan oleh JAKA.\n
                6. Perlu diingat bahwa pengguna JAKA harus mempertimbangkan jumlah SKS maksimum yang dapat diambil pada setiap penyusunan jadwal, karena JAKA menyamaratakan jumlah SKS maksimum untuk setiap mahasiswa, yaitu 24 SKS.\n
            """)
        isAgree = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
        
        loginBtn = st.container()
        
        if isAgree:
            if u and p and not st.session_state['auth']:
                try:
                    st.session_state['auth'] = scraping.app(u, p)
                    if st.session_state['auth']:
                        st.session_state['username'] = u
                        status.success('Authenticated')
                    else:
                        status.error('Wrong username or password')
                except:
                    status.error('Authentication Failed')
                    pass
            elif not st.session_state['auth']:
                status.warning('Username dan Password tidak boleh kosong')
        
        if st.session_state['auth'] and isAgree:
            loginBtn.write(" ")
            loginBtn.button('Login', on_click=goto, args=['Dashboard'])
        else:
            loginBtn.markdown("""
            <a href='javascript:alert("Authenticated User Only! Please, check the User Agreement!");'>
                <div class="row-widget customButton">
                    <button>
                        Login
                    </button>
                </div>
            </a>
            """, unsafe_allow_html=True)

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
        st.button('Iya, yakin.', on_click=reset, args=None)
