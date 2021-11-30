import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def app():
    db = firestore.client()
    
    listCourse = db.collection('users').document(st.session_state['username']).get()
    listCourse = listCourse.to_dict()
    listCourse = listCourse['listCourse']
    
    courses = {}
    st.session_state['selectedCourse'] = []
    
    for course in listCourse:
        getData = db.collection('courses').document(course).get()
        if getData.exists:
            getData = getData.to_dict()
            courses[course] = getData
    
    listCourse.clear()
    
    c1, c2 = st.columns((3, 1))
    
    with c1:
        for course in courses:
            listCourse.append(course+" - "+courses[course]['Nama']) 
        st.subheader('Select Course(s)')
        st.session_state['selectedCourse'] = st.multiselect('', options=listCourse)
        
    with c2:
        for i in range(4):
            st.write(' ')
        
        st.markdown("""
        <style>
        div.stButton > button {
            background-color: #f72585;
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #f8f8f8;
            box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 10px 20px 0 rgba(0,0,0,0.19);
        }
        </style>""", unsafe_allow_html=True)
        
        if st.button('Create Plan'):
            sks = 0
            for course in st.session_state['selectedCourse']:
                sks += int(course[-14:-13])
                print(sks)
                if sks > 24:
                    st.error('Melebihi Maksimum SKS ('+str(sks)+'/24)')
                    return False
            st.success('Total SKS ('+str(sks)+'/24)')
            st.session_state['menu'] = 'Choose Schedule'
            return len(st.session_state['selectedCourse']) > 0
    
def SelectSchedule():
    c1, c2 = st.columns ([3,1])
    db = firestore.client()
    with c1:
        for course in st.session_state['selectedCourse']:
            st.info(course[:10])
            getData = db.collection('courses').document(course[:10]).get()
            getData = getData.to_dict()
            with st.expander(course):
                courseDetails = getData['Kelas']
                cours1 = st.radio('Pilih Kelas yang Diinginkan:', course1_sched, key='cours1')
                
    with c2:
        st.subheader("Jadwal yang telah dipilih per matkul")
        st.write("")
        st.write("")
        st.write("Course 1:", cours1)
        st.write("Course 2:", cours2)
        st.write("Course 3:", cours3)
        st.write("Course 4:", cours4)
        st.write("Course 5:", cours5)
        st.write("Course 6:", cours6)
        st.write("Course 7:", cours7)
        st.write("Course 8:", cours8)
