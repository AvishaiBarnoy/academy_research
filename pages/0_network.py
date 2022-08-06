import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

st.markdown("""
    ## Ideas
    The weight of each edge is the ratio of the amount of professors each institute contributed to the other.
    The size of a node is proporsional to self recruitments.

    look at DiGraph for directed graphs.
    """)

inst_dict = {0:"Haifa", 1:"OpenU", 2:"BIU", 3:"TAU", 4:"Ariel", 5:"Technion", 6:"BGU",
        7:"HUJI", 8:"WIS", 9:"USA", 10:"Europe", 11:"USSR"}

data = pd.read_csv(Path(__file__).parent / "../data/physics_data.csv",index_col=0)
edges = []
G = nx.MultiDiGraph()
#G.add_nodes_from(inst_dict.values())

for i,j in enumerate(data):
    for k,l in enumerate(data):
        if data[l][i] > 0:
            edges.append((i,k,{"weight":data[l][i]}))
G.add_edges_from(edges)

fig, ax =  plt.subplots()
ax = nx.draw(G)
st.pyplot(fig,clear_figure=True)

#fig = go.Figure(data=g)
#st.plotly_chart(fig, use_container_width=True, sharing="streamlit")
