from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import streamlit as st
import re

def app(u, p):
    loading = st.progress(0)
    with st.spinner('Authenticating...'):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        
        driver.get("https://academic.ui.ac.id/")
        
        loading.progress(25)
        
        username = driver.find_element(By.NAME, "u")
        # username.send_keys(sys.argv[1])
        username.send_keys(u)
        
        password = driver.find_element(By.NAME, "p")
        # password.send_keys(sys.argv[2])
        password.send_keys(p)

        login = driver.find_element(By.CSS_SELECTOR, "input[value='Login']")
        login.click()
        
        loading.progress(50)
        
        driver.get("https://academic.ui.ac.id/main/Schedule/Index")

        element = driver.find_element(By.CSS_SELECTOR, "#ti_h")
        
        if element.text != 'Jadwal Kelas Mata Kuliah':
            driver.close()
            return False
        
        page_source = driver.page_source
        
        driver.close()
        
        cuts = []
                
        for m in re.finditer('<table class="box">', page_source):
            cuts.append([m.start(), m.end()])

        iter = 0
        for m in re.finditer('</table>', page_source):
            cuts[iter][1] = m.end()
            iter += 1
            if iter >= len(cuts):
                break
        
        loading.progress(75)
        
        filtered_page = ""
        for i in range(len(cuts)):
            filtered_page += page_source[cuts[i][0]:cuts[i][1]]

        regexDay = '([A-Za-z]+, [0-9]+.[0-9]+-[0-9]+.[0-9]+)'

        soup = BeautifulSoup(filtered_page, 'html.parser')

        courses = soup.find_all("tr")

        elements = ""
        
        for course in courses:
            selected = course.find("th")
            if selected is not None:
                if ";" in selected.text:
                    elements += selected.text
                    elements += "--------------"
            selected = course.find_all("td", nowrap="")
            if len(selected) > 0:
                for element in selected:
                    elements += element.text + "\n"
                elements += "--------------"

        listElements = elements.split("--------------")

        courses = {}

        temp = ""

        for element in listElements:
            element = element.strip()
            if ";" in element and "-" not in element[:11]:
                temp = element[:11].strip()
                temp = temp.strip('\n')
                name = element[13:-28].strip()
                name = name.strip('\n')
                courses.update({
                    temp : {
                        'Nama' : name,
                        'Kelas' : []
                    }
                })
            elif temp != "":
                tempClass = element.split('\n')
                if (len(tempClass) > 1 and ';' in tempClass[1]):
                    break
                elif len(tempClass) > 6 :
                    courses[temp]['Kelas'].append({
                        'Nama' : tempClass[1],
                        'Jadwal' : re.findall(regexDay, tempClass[4]),
                        'Ruang' : tempClass[5].strip("-"), 
                        'Dosen' : tempClass[6].strip("- ").split("- ")
                    })
                elif len(tempClass) > 5 :
                    courses[temp]['Kelas'].append({
                        'Nama' : tempClass[1],
                        'Jadwal' : re.findall(regexDay, tempClass[4]),
                        'Ruang' : tempClass[5].strip("-"), 
                        'Dosen' : ''
                    })
                elif len(tempClass) > 4 :
                    courses[temp]['Kelas'].append({
                        'Nama' : tempClass[1],
                        'Jadwal' : re.findall(regexDay, tempClass[4]),
                        'Ruang' : '', 
                        'Dosen' : ''
                    })
                elif len(tempClass) > 3 :
                    courses[temp]['Kelas'].append({
                        'Nama' : tempClass[1],
                        'Jadwal' : '',
                        'Ruang' : '', 
                        'Dosen' : ''
                    })
        loading.progress(100)
        st.session_state['courses'] = courses
        
        return True
