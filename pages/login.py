import streamlit as st

check_u = 'admin'
check_p = 'admin'

def auth(username, password):
    if username == check_u and password == check_p:
        st.success('Login Successful')
    else:
        st.error('Login Unsuccessful')
    return True

def app():
    st.markdown("<h1 style='text-align: center;'>JAKA</h1>", unsafe_allow_html=True)
    st.markdown("<center><a style='text-align: center;'>Sign in to your SSO-UI account.</a></center>", unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    left, center, right = st.columns([2, 3, 2])
    with center:
        with st.form('login_form', clear_on_submit=False):
            u = st.text_input('Username', max_chars=30)
            p = st.text_input('Password', type='password', max_chars=30)
            with st.expander("Kebijakan Privasi JAKA"):
                st.write("""
                    The chart above shows some numbers I picked for you.
                    I rolled actual dice for these, so they're *guaranteed* to
                    be random.
                """)
            is_agree = st.checkbox('Saya telah membaca dan menyetujui Kebijakan Privasi JAKA')
            is_login = st.form_submit_button('Login')
    if is_agree and is_login:
        return auth(u, p)
    else:
        return False
