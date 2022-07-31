import streamlit as st
import pandas as pd
from scripts.column import col_institute, col_subject
from scripts.present_text import women_text
from pathlib import Path
import plotly.graph_objects as go

st.markdown("""
        # Women Professors in STEM
        """)

intro_text_path = Path(__file__).parent / "../text/women_intro.txt"
women_text(intro_text_path)

path = f"../data/women_stem.csv"
stem_data = pd.read_csv(Path(__file__).parent / path)

# Plot by institute
st.markdown("## By Institute")
institute_text_path = Path(__file__).parent / "../text/women_institute.txt"
women_text(institute_text_path)
institute = st.selectbox("Choose an institute to show data:", ("Ariel", "Ben Gurion", "Bar Ilan", "Hebrew U.", "Weizmann", 
    "Technion", "Tel-Aviv"))
fig_data_inst = st.radio("Show absolute or precetage data in figures", ("precentage", "absolute"))

col_institute(stem_data, institute, fig_data_inst)

# Plot by institute
st.markdown("## By Subject")
subject_text_path = Path(__file__).parent / "../text/women_subject.txt"
women_text(subject_text_path)
subject = st.selectbox("Choose a subject to compare institutes", ("chemistry", "biology", "physics", "math", "cs"))
fig_data_dept = st.radio("Show absolute or precetage data in figures", ("precentage ", "absolute "))

col_subject(stem_data, subject, fig_data_dept)

st.markdown("""- data was collected at the end of 2020""")
