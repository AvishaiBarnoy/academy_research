import pandas as pd
import streamlit as st
import plotly.graph_objects as go

def col_institute(stem_data, institute, kind):
    translation_dict = {"Ariel":"Ariel","Ben Gurion":"BGU","Bar Ilan":"BIU","Hebrew U.":"HUJI","Weizmann":"WIS",
        "Technion":"Technion","Tel-Aviv":"TAU"}
    institute_data = stem_data[stem_data["institute"] == translation_dict[institute]] 
    if kind == "precentage":
        #y_men = institute_data["men"]/institute_data["total"]*100
        y_women = institute_data["women"]/institute_data["total"]*100
        column_fig = go.Figure(data=[
            go.Bar(name="Women", x=institute_data["department"], y=y_women)
            ],
            layout_title=f"Women in STEM by Institution {kind}")
    elif kind == "absolute":
        y_men = institute_data["men"]
        y_women = institute_data["women"]
        column_fig = go.Figure(data=[
            go.Bar(name="Women", x=institute_data["department"], y=y_women),
            go.Bar(name="Men", x=institute_data["department"], y=y_men)
            ],
            layout_title=f"Women in STEM by Institution {kind}")
    if kind == "precentage": column_fig.update_yaxes(range=[0,100])
    st.plotly_chart(column_fig, use_container_width=False,sharing="streamlit")
    st.caption(f"Women in different STEM departments at {institute}, {kind}.")

def col_subject(stem_data, subject, kind):
    subject_dict = {"chemistry":"Chemistry","biology":"Biology","physics":"Physics","math":"Math","cs":"Computer Science"}
    subject_data = stem_data[stem_data["department"]==subject]
    if kind == "precentage ":
        #y_men = subject_data["men"]/subject_data["total"]*100
        y_women = subject_data["women"]/subject_data["total"]*100
        column_fig = go.Figure(data=[
            go.Bar(name="Women", x=subject_data["institute"], y=y_women)
            ],
            layout_title=f"Researchers in {subject_dict[subject]} by Institute {kind}")
    elif kind == "absolute ":
        y_men = subject_data["men"]
        y_women = subject_data["women"]
        column_fig = go.Figure(data=[
            go.Bar(name="Women", x=subject_data["institute"], y=y_women),
            go.Bar(name="Men", x=subject_data["institute"], y=y_men)
            ],
            layout_title=f"Researchers in {subject_dict[subject]} by Institute {kind}")
    if kind == "precentage ": column_fig.update_yaxes(range=[0,100])
    st.plotly_chart(column_fig, use_container_width=False,sharing="streamlit")
    st.caption(f"Women in {subject} by institute, {kind}.")
