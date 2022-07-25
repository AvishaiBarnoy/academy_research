import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def col_institute(stem_data, institute, kind):
    translation_dict = {"Ariel":"Ariel","Ben Gurion":"BGU","Bar Ilan":"BIU","Hebrew U.":"HUJI","Weizmann":"WIS",
        "Technion":"Technion","Tel-Aviv":"TAU"}
    institute_data = stem_data[stem_data["institute"] == translation_dict[institute]] 
    column_fig = go.Figure(data=[
        go.Bar(name="Women", x=institute_data["department"], y=institute_data["women"]/institute_data["total"]*100),
        go.Bar(name="Men", x=institute_data["department"], y=institute_data["men"]/institute_data["total"]*100)
        ],
        layout_yaxis_range = [0,100],
        layout_title="Precentage of Women in STEM by Institution")
    st.plotly_chart(column_fig, use_container_width=False,sharing="streamlit")
    st.caption(f"Precentage of women in different STEM departments at {institute}.")

def col_subject(stem_data, subject, kind):
    subject_dict = {"chemistry":"Chemistry","biology":"Biology","physics":"Physics","math":"Math","cs":"Computer Science"}
    subject_data = stem_data[stem_data["department"]==subject]

    if kind == "precentage ": 
        column_fig = go.Figure(data=[
            go.Bar(name="Women", x=subject_data["institute"], y=subject_data["women"]/subject_data["total"]*100),
            go.Bar(name="Men", x=subject_data["institute"], y=subject_data["men"]/subject_data["total"]*100)
            ],
            layout_yaxis_range = [0,100],
            layout_title=f"{kind.capitalize()} of Researchers in {subject_dict[subject]} by Institute")
        st.plotly_chart(column_fig, use_container_width=False,sharing="streamlit")
        st.caption(f"Precentage of women in {subject} by institute.")
    elif kind == "absolute ": 
        column_fig = go.Figure(data=[
            go.Bar(name="Women", x=subject_data["institute"], y=subject_data["women"]),
            go.Bar(name="Men", x=subject_data["institute"], y=subject_data["men"])
            ],
            layout_title=f"{kind.capitalize()} of Researchers in {subject_dict[subject]} by Institute")
        st.plotly_chart(column_fig, use_container_width=False,sharing="streamlit")
        st.caption(f"Precentage of women in {subject} by institute.")
    #column_fig.update_yaxes(range=[0,100])
