import streamlit as st
import networkx as nx
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from pathlib import Path
import pandas as pd

st.markdown("""
    # Network Analysis - Under Construction
    This section is under construction and therefore includes, thoughts, ideas and half-backed results.
    ## Ideas
    The weight of each edge is the ratio of the amount of professors each institute contributed to the other.
    The size of a node is proporsional to self recruitments.

    look at DiGraph for directed graphs.
    """)

inst_dict = {0:"Haifa", 1:"OpenU", 2:"BIU", 3:"TAU", 4:"Ariel", 5:"Technion", 6:"BGU",
        7:"HUJI", 8:"WIS", 9:"USA", 10:"Europe", 11:"USSR"}

subject = st.selectbox("Choose a subject for analysis:",("chemistry","physics"))
data = pd.read_csv(Path(__file__).parent / f"../data/{subject}_data.csv",index_col=0)
edges = []
G = nx.MultiDiGraph()
G.add_nodes_from(inst_dict.values())

for i,j in enumerate(data):
    for k,l in enumerate(data):
        if data[l][i] > 0:
            edges.append((j,l,{"weight":data[l][i]}))
G.add_edges_from(edges)

fig, ax =  plt.subplots()

#ax = nx.draw_networkx(G) # draws numbers
#ax = nx.draw_circular(G) # prettier
#ax = nx.draw_shell(G) # looks like circular
#ax = nx.draw_kamada_kawai(G)
#st.pyplot(fig,clear_figure=True)

inst_dict = {0:"Haifa", 1:"OpenU", 2:"BIU", 3:"TAU", 4:"Ariel", 5:"Technion", 6:"BGU",
        7:"HUJI", 8:"WIS", 9:"USA", 10:"Europe", 11:"USSR"}
num_to_inst = {"Haifa":0, "OpenU":1, "Bar Ilan":2, "Tel-Aviv":3, "Ariel":4, "Technion":5, "Ben Gurion":6,
        "Hebrew":7, "Weizmann":8, "USA":9, "Europe":10, "USSR":11}

institute = st.selectbox("Choose an institute to show data:", ("Haifa", "OpenU", "BIU", "TAU", "Ariel", "Technion",
    "BGU", "HUJI", "WIS", "USA", "Europe", "USSR"))



# TODO: Algorithms to check
#   1. pagerank - num researchers is the in/out number of links
#   2. voterank - researchers can be used as "vote", check documentation for diGraph variation
#   3. trophic_level - 1st read Levine's paper to understand the algorithm
#   4. 

# TODO: check weights for degree analysis
st.write(f""" ### Degree
    The degree of {institute} is {G.degree[institute]}
    
    Degree is the number of edges adjacent to the node, since the figure is a mulitdirectional directed graph both in and
    out are counted. Weights for the edges are not implemented yet.
    
    
    Also, there is a double counting of each institute by itself.
    """)

# TODO: check current-flow-closeness
st.write(f""" ### Centrality
    The centrality of {institute} is {round(nx.degree_centrality(G)[institute],2)}

    The in-degree-centrality of {institute} is {round(nx.in_degree_centrality(G)[institute],2)}

    The out-degree-centrality of {institute} is {round(nx.out_degree_centrality(G)[institute],2)}

    in/out degree of centrality is the normalized amount of in/out edges of each node.

    """)

#The problem with degree is that it only counts the number of edges between nodes but does not apply weigths to them.
#Weights should be added, though I am not sure yet as to how to do it. How to normalize the weights, and how to take
#into accounts professors that graduated in the same institute they got their position in.
#Weights are possible for _G.degree_, one should explore this option.

#Centrality is normalized by possible number of edges but not for the weight of each edge for directed graphs and 
#multi-graphs, therefore it is an important measure but not enough.
