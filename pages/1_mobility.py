import streamlit as st
from pathlib import Path
from scripts.sankey import sankey

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
    This section will show two (currently only one) sankey graphs. One for physicsts and 
    another for chemsits. Each graph shows where the PI's from different institutions studied
    for their PhD and where they were accepted for their current tenure track.

    Data was collected on 2021 and is only relevant for active members without emeritii.
""")

subject = st.sidebar.radio("Select subjec to show flow", ("Physics", "Chemistry"))
if subject == "Physics":
    path = "../data/physicists.txt"
    sank_fig = sankey(Path(__file__).parent / path, subject)
    st.write(f" ## {subject.capitalize()}")
    st.plotly_chart(sank_fig,use_container_width=False,sharing="streamlit")
    st.caption(f"""{subject.capitalize()} PI's flow. On the left where PI's studied and on the right where they got their tenure
            position.""")
    st.write("""
        ### Analysis
        Each institute (except Ariel and BGU) has the highest precentage of researchers from the same institue.
        This would make sense as researchers already know the candidate and if he's goog enough he will be accepted.
        I don't understand why in BGU only 5% of the physics faculty studied at BGU. Ariel makes sense as it is still
        a very young institution. On the other side there is WIS with 54% faculty who studied at WIS. HUJI is at 30% HUJI
        and 30% WIS, while TAU and Technion have a higher precentage of TAU and Technion than WIS recpetvially.
        
        Looking at raw numbers WIS trained 38% of Israeli trained physicists, TAU coming $2^{nd}$ with 23%. When on takes
        into account people who studied abroad the number changes, yet WIS still holds the lead.

        There is still a strong presence of professors who studied at the USSR being 5.6% of the faculty. Where BIU
        having 13% and TAU, WIS, and HUJI having only 2% USSR faculty. This also is not suprising and these faculty
        members are mostly at the
        ages of 60.
        
        ### Thoughts
        Why do we see such trends? Is this a relevant metric to compare universities?

        This data is incomplete, how many physcists work in other faculties? Maybe WIS is extremly good ad training
        physicists that get into physics departments while the Technion trains those who get into Life Sciences departments?
        This will be partly answered when I will have the time to analyze the chemistry departments data.
        
        What is the variance of PhD students quality between institutes? Students tend inertially contniune to grad school
        at the same institute where they did their undergraduate studies. How do students choose where to study their bachelors
        degree? So many questions left unanswered, but they are vital for the flourish of an institution as without good grad
        students research cannot move forward.
        Finally, as in every competitive field the fight is not over students, but over the good ones.
    """)
elif subject == "Chemistry":
    try:
        path = "../data/chemistry.txt"
        sank_fig = sankey(Path(__file__).parent / path, subject)
        st.write(f" ## {subject.capitalize()} ")
        st.plotly_chart(sank_fig,use_container_width=False,sharing="streamlit")
    except FileNotFoundError as e:
        st.error(f"""
            Data file for {subject} does not exist yet.
            {e}
        """)
