from numpy import select
from requests.sessions import session
import streamlit as st

def goto(page):
    st.session_state['menu'] = page

def updateCourse():
    if 'selected' in st.session_state:
        st.session_state['selectedCourse'] = st.session_state['selected']

def Course():
    courses = st.session_state['courses']
    
    headerTxt, continueBtn = st.columns([4, 1])
    headerTxt.header('Select Course(s)')
    
    st.write("---")
    
    filter, status = st.columns([4, 1])
    
    listCourse = []
    
    with filter:
        for course in courses:
            listCourse.append(course+" - "+courses[course]['Nama']) 
        st.multiselect('Type or scroll to search', options=listCourse, default=st.session_state['selectedCourse'], key='selected', on_change=updateCourse)    
        
    sks = 0
    for course in st.session_state['selectedCourse']:
        sks += int(course[-14:-13])
    
    status.metric(label="SKS", value=sks, delta=(24 - sks))
    
    st.write("---")
    with st.expander("Selected Course", expanded=True):
        for selected in st.session_state['selectedCourse']:
            st.write(selected)
    
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
                background-color: #3a0ca3;
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
    headerTxt, backBtn, saveBtn = st.columns([4, 1, 1])
    headerTxt.header('Select Class')
    
    if 'selectedCourse' in st.session_state:
        temp = st.session_state['selectedCourse']
    
    st.write("---")
    
    optHead, schedHead, lectHead = st.columns([3, 2, 3])
    
    optHead.markdown("<p><h3 align='center'>Class</h3></p>", unsafe_allow_html=True)
    schedHead.markdown("<p><h3 align='center'>Schedule</h3></p>", unsafe_allow_html=True)
    
    lectHead.markdown("<p><h3 align='center'>Lecturer</h3></p>", unsafe_allow_html=True)
    
    for courseName in temp:
        courseCode = courseName[:10].strip()
        with st.expander(courseName, True):
            data = st.session_state['courses'][courseCode]['Kelas']
            with st.container():
                opt, sched, lect = st.columns([3, 2, 3])
                
                for i in range(3):
                    sched.write(" ")
                    lect.write(" ")
                
                indexClass = 0
                option = []
                
                if len(data) > 1:
                    option = ['Rekomendasi JAKA']                        
                        
                    if courseCode not in st.session_state:
                        st.session_state[courseCode] = 'Rekomendasi JAKA'
                else:
                    opt.write(" ")
                    st.session_state[courseCode] = data[0]['Nama']
                
                for kelas in data:
                    temp = kelas['Nama']
                    option.append(temp)
                    
                    for jadwal in kelas['Jadwal']:
                        sched.markdown("<li align='center'>"+jadwal+"</li>", unsafe_allow_html=True)
                    
                    for dosen in kelas['Dosen']:
                        lect.markdown("<li align='center'>"+dosen+"</li>", unsafe_allow_html=True)
                
                indexClass = option.index(st.session_state[courseCode])
                opt.radio(' ', options=option, key=courseCode, index=indexClass)        
    
    noConflict = False
    
    with backBtn:
        st.write(" ")
        st.button('Back', on_click=goto, args=['Create Schedule'])
    
    with saveBtn:        
        if noConflict:
            st.write(" ")
            st.button('Save', on_click=goto, args=['Save Schedule'])
        else:
            st.markdown("""
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700;800&display=swap" rel="stylesheet">
            <style>
            div.disabledButton > button {
                background-color: #3a0ca3;
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
                Save
                </button>
                </div>
            ''', unsafe_allow_html=True)