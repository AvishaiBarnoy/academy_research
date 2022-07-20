import streamlit as st
import pandas as pd
from scripts.column import column
from pathlib import Path
import plotly.graph_objects as go

st.markdown("""
        # Under construction
        """)

path = f"../data/women_stem.csv"
stem_data = pd.read_csv(Path(__file__).parent / path)
#st.table(stem_data)

institute = st.sidebar.radio("Select institute to show women", ("Ariel", "Ben Gurion", "Bar Ilan", "Hebrew U.", "Weizmann",
    "Technion", "Tel-Aviv"))
translation = {"Ariel":"Ariel","Ben Gurion":"BGU","Bar Ilan":"BIU","Hebrew U.":"HUJI","Weizmann":"WIS",
        "Technion":"Technion","Tel-Aviv":"TAU"}
inst = translation[institute]

part = stem_data[stem_data["institute"] == inst]
#st.table(part)


# Eventually move to individual function
column_fig = go.Figure(data=[
    go.Bar(name="Women", x=part["department"], y=part["women"]/part["total"]*100),
    go.Bar(name="Men", x=part["department"], y=part["men"]/part["total"]*100)
    ],
    layout_yaxis_range=[0,100],
    layout_title="Precentage of Women in STEM by Institution")
st.plotly_chart(column_fig, use_container_width=False,sharing="streamlit")
st.caption(f"Precentage of women in different STEM departments at {inst}.")



st.markdown("""- data was collected at the end of 2020""")
