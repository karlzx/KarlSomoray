import streamlit as st
import pandas as pd
import numpy as np

import pydeck as pdk


class ExperienceHandler():
    def __init__(self):
        self.tags = pd.Series(['All'])
        self.experiences = []
        self.education = []
    


    def add_experience(self,jobtitle, fromdate, todate, company, description, tags):
        self.experiences.append( self.Experience(jobtitle, fromdate, todate, company, description,tags))

        self.tags = self.tags.append(pd.Series(tags), ignore_index= True)
        # self.tags = self.tags.unique

        # self.tags.append(, ignore_index = True)
        # self.tags = self.tags.unique()
        self.tags = pd.Series(self.tags.unique())
    
    def write_tags(self):
        self.tags_chosen = st.multiselect('Select Experience Categories', 
           self.tags, default = 'All')


    def add_education(self,study, from_date, to_date, uni, description):
        self.education.append( self.Education(study, from_date, to_date, uni, description))
    


    def write_education(self):
        for edu in self.education:
            st.markdown('**{0}** - _{1} - {2}_  \n{3}'.format(edu.study, edu.from_date, edu.to_date, edu.uni))
            st.write("""
            {0}
            """.format(edu.description))
            st.write('_____________________________________________________')

    def write_experience(self):
        for exp in self.experiences:
            if any(x in self.tags_chosen for x in exp.tags) or 'All' in self.tags_chosen:
                st.markdown('**{0}** - _{1} - {2}_  \n{3}'.format(exp.jobtitle, exp.from_date, exp.to_date, exp.company))
                st.write("""{0}""".format(exp.description) )
                st.caption("""_Tags: {0}_""".format(', '.join([str(elem) for elem in exp.tags])))
    
                
                st.write('_____________________________________________________')


    class Experience():
        def __init__(self,jobtitle, from_date, to_date, company, description, tags):
            self.jobtitle = jobtitle
            self.from_date = from_date
            self.to_date = to_date
            self.company = company
            self.description = description
            self.tags = tags
    
    class Education():
        def __init__(self,study, from_date, to_date, uni, description):
            self.study = study
            self.from_date = from_date
            self.to_date = to_date
            self.uni = uni
            self.description = description


def prefill_experiences(eH):
    eH.add_experience("Data Project Officer", "Aug 2021", "Present", "Queensland University of Technology", """
        > Developing a Power BI (Data Analytics) Dashboard for the QUT Academy of Learning and Teaching (QALT) Team.

        > Supporting research project on the development of language processing tools for textual analysis.    """, ['Data Analytics','Python', 'PowerBI'])

    eH.add_experience("Sessional Academic (Tutor)", "Mar 2021", "Dec 2021", "Queensland University of Technology", """
    > Facilitate workshops and computer labs for First-Year engineering students.

    > Deliver content to cater students from a wide variety of backgrounds and skill sets.

    > Tutored:

    > MZB125 - Introductory Engineering Mathematics

    > MZB126 - Engineering Computation    """, ['Teaching', 'MATLAB'])

    eH.add_experience("STEM Student Ambassador", "Feb 2018", "Dec 2021", "Queensland University of Technology", """
    > Facilitate workshops and campus tours to High School students that visit the university.

    > Maintain a strong knowledge of topics covered in Science, Technology, Engineering and Mathematics (STEM), evaluating presentation content and style to match the appropriate age groups.   
    """, ['Teaching'])

    eH.add_experience("Software Intern", "Jan 2020", "Jun 2020", "Deswik", """
    > Assisted in development of UI and interactive elements for Deswik's optimization suites using C#/.NET.

    > Used source control methods (GIT) and project management platforms (JIRA).
    > Interacted with various teams to meet sprint deadlines and UX requirements,
    """, ['Engineering - Software', 'C#'])


    eH.add_experience("Project Engineer (Intern) - Manufacturing Engineering", "Nov 2018", "May 2019", "VDL Nedcar", """
    > Investigated the implementation of an automated workload balancing system for the BMW and MINI assembly line.

    > Developed a data entry strategy and sorting algorithm that enables scheduling of jobs to a specified assembly line layout, based on the pre-exisiting data format.

    > Demonstrated feasibility of converting the manual task of scheduling into an automated task.

    > Created a visualisation tool to discretely model and simulate the line-balancing strategy.  
    """, ['Data Analytics', 'MATLAB', 'Simulation', 'Algorithm', 'Engineering - Software'])

    eH.add_experience("Retail Assistant", "Dec 2015", "Nov 2018", "City Beach Australia", """
    > Quickly responded to manager’s requests and maintained a good relationship with other team members.

    > Worked efficiently in various roles (as a general floor assistant, stock processor, counter staff, and salesannouncer) leading to reduced workloads for the following staff.
    """, ['Retail', 'Customer Facing'])

    eH.add_education("Bachelor of Engineering (Honours)/Bachelor of Mathematics", "Jan 2016", "Nov 2021", "Queensland University of Technology", """
            > * First Class Honours and Distinction

            > * John Kindler Memorial medal
            """)
    eH.add_education("Engineering Module (International Summer University)", "Jun 2018", "Jul 2018", "University of Kassel", """
    > * Adaptation Strategies to Climate Change
    > * Environmental Engineering and Renewable Energies
    > * German (Beginner)
    """)
