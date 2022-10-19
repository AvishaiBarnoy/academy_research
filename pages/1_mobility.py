import streamlit as st
from pathlib import Path
from scripts.sankey import sankey
import scripts.present_text as pt
import scripts.nopa as nopa

st.markdown(""" # Academic Mobility """)

subject = st.radio("Select a research field to show flow data for", ("Physics", "Chemistry"))
path = f"../data/{subject.lower()}_data.txt"

sank_fig = sankey(Path(__file__).parent / path, subject)
st.write(f" ## {subject.capitalize()}") # subject title -> pt_text_intro_subject
pt.text_intro_subject(subject)

nepotism_ind = nopa.nopa(Path(__file__).parent / path)
import numpy as np
import pandas as pd
st.write(f"""
        ## Nepotism Index
        The nepotism index for {subject} is:
        """)
st.table(nepotism_ind)

st.plotly_chart(sank_fig,use_container_width=False,sharing="streamlit")

# methodology
st.markdown("""
        I looked at PI's in physics and chemistry where they did their PhD and where they got their 
        tenure track position. This can teach us on the mobility of ideas culture between peoples
        alma mater and where they finally got their office.

        One can speculate about these effects, their source, and their impact. Does a student thinking 
        of an academic career plan his graduate school according to such figure? I don't believe so, but
        he should try and think of the reasons we see such trends. How does the Weizmann institution 
        train so many physicists? Ariel trained only 1 but that would make sense, since they're a very
        young university.
        """)

pt.text_sankey_analysis(subject) # show analysis for {subject}

st.write("""
    ### Disclaimer
    Data was collected on 2021 from the faculty web-pages of the institutes. Presente data takes into account
    only researchers in a tenure track without emeritii.
""")
