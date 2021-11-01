import streamlit as st

courses = [
    {
        'name'  : 'Course 1',
        'sks'   : 3,
        'term'  : 4,
        'sched' : [
                    'Rekomendasi Jaka'
                    ,'MON13001500'
                    ,'TUE13001500'
                  ],
        'selected' : 'No'
    },
    {
        'name'  : 'Course 2',
        'sks'   : 3,
        'term'  : 4,
        'sched' : [
                    'Rekomendasi Jaka'
                    ,'MON13001500'
                    ,'TUE13001500'
                  ],
        'selected' : 'No'
    }
]

def FilterCourse():
    c1, c2 = st.columns((3, 1))
    with c1:
        course_list = []
        for course in courses:
            course_list.append(course['name']+' ('+str(course['sks'])+')') 
        st.subheader('Select Course(s)')
        course_selected = st.multiselect('', options=course_list)
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
            for course_name in course_selected:
                for course in courses:
                    if course['name'] == course_name[:-4]:
                        course['selected'] = 'Yes'
                        break
            return True
    
def SelectSchedule():
    c1, c2 = st.columns((3, 1))
    with c1:
        st.subheader('Course Schedule')
        for course in courses:
            if course['selected'] == 'Yes':
                with st.expander(course['name']):
                    course['selected'] = st.radio('Pilih Jadwal', options=course['sched'], key=course['name'])
            
    with c2:
        st.subheader('Course Plan')
        for course in courses:
            if course['selected'] in course['sched']:
                st.info(course['name'] + ' : ' + course['selected'])

def app():
    if FilterCourse():
        SelectSchedule()