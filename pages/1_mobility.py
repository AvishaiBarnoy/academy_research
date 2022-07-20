import streamlit as st
from pathlib import Path
from scripts.sankey import sankey
import scripts.present_text as pt

st.markdown("""
        # Academic Mobility
        I looked at PI's in physics and chemistry where they did their PhD and where they got their 
        tenure track position. This can teach us on the mobility of ideas culture between peoples
        alma mater and where they finally got their office.

        One can speculate about these effects, their source, and their impact. Does a student thinking 
        of an academic career plan his graduate school according to such figure? I don't believe so, but
        he should try and think of the reasons we see such trends. How does the Weizmann institution 
        train so many physicists? Ariel trained only 1 but that would make sense, since they're a very
        young university.

        This section of the research is, currently, only descriptive. But one can try and suggest reasons
        for the trends seen.
        """)

st.sidebar.header("Sankey Graphs")
st.write("""
    This section will show two sankey graphs. One for physicsts and another for chemsits. Each graph shows
    where the PI's from different institutions studied for their PhD and where they were accepted for their
    current tenure track.

    Data was collected on 2021 and is only relevant for active members without emeritii.
""")

subject = st.sidebar.radio("Select subject to show flow", ("Physics", "Chemistry"))
path = f"../data/{subject.lower()}_data.txt"

sank_fig = sankey(Path(__file__).parent / path, subject)
st.write(f" ## {subject.capitalize()}") # subject title

pt.text_intro_subject(subject)

st.plotly_chart(sank_fig,use_container_width=False,sharing="streamlit")
st.caption(f"""{subject.capitalize()} PI's flow. On the left where PI's studied and on the right where they got their tenure
    position.""")

pt.text_sankey_analysis(subject)
