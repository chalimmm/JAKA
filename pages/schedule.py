import streamlit as st

def goto(page):
    st.session_state['menu'] = page

def checkSKS():
    sks = 0
    for course in st.session_state['selectedCourse']:
        sks += int(course[-14:-13])
        print(sks)
        if sks > 24:
            st.error('Melebihi Maksimum SKS ('+str(sks)+'/24)')
            return False
    st.success('Total SKS ('+str(sks)+'/24)')
    return True

def FilterCourse():
    courses = st.session_state['courses']
    st.session_state['selectedCourse'] = []
    
    filter, confirm = st.columns((3, 1))
    
    listCourse = []
    
    with filter:
        for course in courses:
            listCourse.append(course+" - "+courses[course]['Nama']) 
        
        st.header('Select Course(s)')
        st.session_state['selectedCourse'] = st.multiselect(' ', options=listCourse)
        
    with confirm:
        for i in range(5):
            st.subheader(" ")
        if len(st.session_state['selectedCourse']) > 0 and checkSKS():
            if st.button('Continue'):
                goto('Choose Schedule')
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
    
def ChooseSchedule():
    control, space, view = st.columns ([4,1,2])
    
    with control:
        st.header('Choose Class')
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
