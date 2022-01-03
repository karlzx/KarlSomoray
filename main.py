import helperfns as hf 
import streamlit as st
import pandas as pd
import numpy as np

import pydeck as pdk

### BACKEND STUFF
eH = hf.ExperienceHandler()
hf.prefill_experiences(eH)
### DISPLAY
options = ('Home', 'Experience', 'Projects - Europe Trip Data')

page = st.sidebar.selectbox('Please select a page',options)
st.sidebar.write('LinkedIn: in/karlsomoray/')

if page == options[0]:
    st.title('Hi! My name is Karl')
    st.write('Engineering and Mathematics Graduate from QUT ')

elif page == options[1]:
    st.title('Education and Experience')
    with st.expander("Click to view Education", expanded = True):
        st.subheader("Education")
        eH.write_education()
        

    with st.expander("Click to view Experience", expanded = True):
        eH.write_tags()
        st.subheader('Experience')
        eH.write_experience()
        
    

elif page == options[2]:
    st.title('Project - Europe Trip Data')





