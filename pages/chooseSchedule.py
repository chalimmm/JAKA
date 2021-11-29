import streamlit as st
import requests
from pages import error

#def createSchedule():
    #st.session_state['menu'] = 'Schedule'

def app():
    c1, c2 = st.columns ([3,1])
    
    with c1:
        with st.expander("Course 1"):
            course1_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours1 = st.radio('Pilih Kelas yang Diinginkan:', course1_sched, key='cours1')
    
        with st.expander("Course 2"):
            course2_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours2 = st.radio('Pilih Kelas yang Diinginkan:', course2_sched, key='cours2')
        
        with st.expander("Course 3"):
            course3_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours3 = st.radio('Pilih Kelas yang Diinginkan:', course3_sched)
    
        with st.expander("Course 4"):
            course4_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours4 = st.radio('Pilih Kelas yang Diinginkan:', course4_sched)
    
        with st.expander("Course 5"):
            course5_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours5 = st.radio('Pilih Kelas yang Diinginkan:', course5_sched)
    
        with st.expander("Course 6"):
            course6_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours6 = st.radio('Pilih Kelas yang Diinginkan:', course6_sched)
    
        with st.expander("Course 7"):
            course7_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours7 = st.radio('Pilih Kelas yang Diinginkan:', course7_sched)
    
        with st.expander("Course 8"):
            course8_sched = ['Hari Pertama', 'Hari Kedua', 'Pilih sesuai rekomendasi dari JAKA']
            cours8 = st.radio('Pilih Kelas yang Diinginkan:', course8_sched)
    
    with c2:
        st.write("Jadwal yang telah dipilih per matkul")
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
