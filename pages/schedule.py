import streamlit as st

def goto(page):
    st.session_state['menu'] = page

def Course():
    courses = st.session_state['courses']
    st.session_state['selectedCourse'] = []
    
    headerTxt, continueBtn = st.columns((4, 1))
    headerTxt.header('Select Course(s)')
    
    filter, status = st.columns((4, 1))
    
    listCourse = []
    
    with filter:
        for course in courses:
            listCourse.append(course+" - "+courses[course]['Nama']) 
        st.session_state['selectedCourse'] = st.multiselect('Type or scroll to search', options=listCourse)
    
    for i in range(5):
        st.write(" ")
        
    sks = 0
    for course in st.session_state['selectedCourse']:
        sks += int(course[-14:-13])
    status.metric(label="SKS", value=str(sks), delta=str(24 - sks))
    
    with continueBtn:        
        if sks in range(1, 25):
            st.write(" ")
            st.button('Continue', on_click=goto, args=['Choose Schedule'])
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
                Continue
                </button>
                </div>
            ''', unsafe_allow_html=True)
    
def Class():
    st.header('Select Class')
    control, space, view = st.columns ([4,1,2])
    with control:
        # st.write(st.session_state['courses'])
        for course in st.session_state['selectedCourse']:
            data = st.session_state['courses'][course[:10].strip()]
            with st.expander(course):
                selected = st.container()
                if len(data['Kelas']) > 1:
                    option = ['Rekomendasi JAKA']
                else:
                    option = []
                for kelas in data['Kelas']:
                    temp = kelas['Nama']
                    option.append(temp)
                    st.write(kelas)
                selected.radio('Pilih Kelas', options=option, key=course)
                
    with view:
        st.header("Overview")
        st.write("")
        st.write("")
