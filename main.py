import helperfns as hf 
import streamlit as st
import pandas as pd
import numpy as np
import os
import pydeck as pdk
from PIL import Image

st.set_page_config(layout="centered")
### BACKEND STUFF
eH = hf.ExperienceHandler()
hf.prefill_experiences(eH)


### DISPLAY

## SIDEBAR
options = ('Home', 'Experience', 'Education' , 'Projects - Europe Trip Data')
page = st.sidebar.selectbox('Please select a page',options)
st.sidebar.write('LinkedIn: in/karlsomoray/')


## PAGES

if page == options[0]:
    col1, col2 = st.columns(2)
    with col2:
        image = Image.open("https://github.com/karlzx/KarlSomoray/blob/main/Images/Selfie.jpg")
        st.image(image)
        
    with col1:
        st.title('Karl Somoray')
        st.write('Engineering and Mathematics Graduate from QUT ')
        st.write("""Passionate about Mechatronics, Data Analytics and Simulation. Please browse through my page to view my past professional and volunteer work,
         as well as some projects that I've worked on including Data, Engineering, Mathematics  \n  \nThis website was built from scratch using the Streamlit API""")

    st.write('__________')
    st.subheader("Coding Experience:")
    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric(label="C/Python", value="1 Year")
    with col4:
        st.metric(label="MATLAB", value="5+ Years")
    with col5:
        st.metric(label="C#", value="1 Year")
    st.write('__________')
    st.subheader("Technical Skills:")
    st.write("**_Engineering_**")
    st.write("3D/PCB Design, Robot Mechanics and Logic, Project Management and Reporting")
    st.write("**_Mathematics_**")
    st.write("Simulation, Algorithm Design, Environment Modelling")
    st.write("**_Data Analytics_**")
    st.write("Power BI, Automation, Data Visualisation")
    st.write("**_Software Development_**")
    st.write("Jira, GIT, Object-Oriented Programming, .NET")
    st.write('__________')
elif page == options[1]:
    st.title('Experience')
    # col1, col2 = st.columns(2)

    # with col1: 
    with st.expander("Click to view Professional Experience", expanded = True):
        st.subheader('Professional Experience')
        eH.write_tags()
        eH.write_experience()
    with st.expander("Click to view Volunteer Experience", expanded = True):
        st.subheader('Volunteer Experience')
        eH.write_vol_tags()
        eH.write_vol_experience()
        
elif page == options[2]:
    st.subheader("Education")
    eH.write_education()

elif page == options[3]:
    st.title('Project - Europe Trip Data')
    st.write("Work In Progress")





