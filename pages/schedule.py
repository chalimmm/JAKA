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
    
    with st.form('selectCourse'):
        for course in courses:
            listCourse.append(course+" - "+courses[course]['Nama']) 
        st.subheader('Select Course(s)')
        st.session_state['selectedCourse'] = st.multiselect('', options=listCourse)
        
        if st.form_submit_button('Create Plan'):
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
            getData = db.collection('courses').document(course[:10]).get()
            getData = getData.to_dict()
            with st.expander(course):
                courseDetails = getData['Kelas']
                selected = st.selectbox('Pilih Kelas', options=courseDetails, key=course[:10])
                
    with c2:
        st.subheader("Jadwal yang telah dipilih per matkul")
        st.write("")
        st.write("")
