import streamlit as st
import scripts.plot_trend_graduate as ptg

st.write("""
        # Trends in Graduation - Under Construction
        Trends in graduation in chemistry and physics (maybe more in the future), for PhD, MSc, and BSc
        between different universities, and maybe also trends in men/women in different subjects.
        """)


subject_list = ["physics", "chemistry", "biology"]
degree_list = ["BSc", "MSc", "PhD"]

subject = st.radio("Select a research field to show data for", subject_list)
all_degrees = ptg.plot_all_degrees_for_subject(subject, degree_list)
st.pyplot(all_degrees)

degree = st.radio("Select degrees to show data for", degree_list)
trend_plot = ptg.plot_by_gender(subject, degree)
st.pyplot(trend_plot)


institute_list = ["Ariel", "OpenU", "WIS", "BGU", "Haifa", "BIU", "TAU", "Technion", "HUJI"] 
institute = st.selectbox("Choose an institute", institute_list) 
by_institution = ptg.plot_by_institute(institute, subject)
st.pyplot(by_institution)

old_subject_data = st.radio("Choose parent science field", ["physical", "biological"])
test = ptg.plot_old_data_graduation_all(old_subject_data, degree_list)
st.pyplot(test)

st.markdown("""
    - data was collected from the Israeli Central Bureau of Statistics
    - biology section includes all life sciences and agrictulture""")
