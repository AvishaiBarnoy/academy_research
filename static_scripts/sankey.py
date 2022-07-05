# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 22:32:02 2022

@author: avish
"""

import plotly.graph_objects as go

FILENAME = "data_no_emeritus.txt"
# open data
with open(FILENAME) as f:
    lines = [line.strip().split("\t") for line in f.readlines()]

link_colors = ['#EBBAB5', '#A6E3d7', '#FEF3C7', '#CBB4D5', '#EC7063', '#48C9B0', '#AF7AC5']
#node_colors = ['#808B96', '#F7DC6F', '#48C9B0', '#AF7AC5', '#EC7063', '#48C9B0', '#AF7AC5']
color_node = ['#808B96',"#F7Dc6F"]
color_link = []
node_colors = ["#003f5c","#2f4b7c","#665191","#a05195","#d45087","#f95d6a","#ff7c43","#ffa600"]


labels = lines[0] + [line[0] for line in lines[1:]]   # create labels
source = []
target = []
value = []
for i,j in enumerate(lines[1:]):
    for k in range(len(lines[0])):
        source.append(i+len(lines[0]))
        target.append(k)
        value.append(j[k+1])
        color_link.append(link_colors[k])
        #color_node.append(link_colors[k])

#print(len(source),len(target),len(value))
#print(source,"\n",target,"\n",value)

link = dict(source=source, target=target, value=value, color=color_link)
node=dict(pad=15, thickness=5,
        line=dict(color="black", width=0.5),
        label=labels,color="black")
data = go.Sankey(link=link, node=node)
fig = go.Figure(data)
title="Physics PI and where they did their Phd"
fig.update_layout(title_text=title, font_size=10)
fig.write_image("sankey_no_emeritus_test.png")
