import plotly.graph_objects as go
import streamlit as st

def read_data(filepath):
    with open(filepath) as f:
        lines = [line.strip().split("\t") for line in f.readlines()]
    return lines

def sankey(filepath, subject):
    """
    takes absolute path for data and subject
    returns plotly figure object
    """
    lines = read_data(filepath)
    link_colors = ['#EBBAB5', '#A6E3d7', '#FEF3C7', '#CBB4D5', '#EC7063', '#48C9B0', '#AF7AC5']
    color_link = []

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

    link = dict(source=source, target=target, value=value, color=color_link)
    node=dict(pad=15, thickness=5,
        line=dict(color="black", width=0.5),
        label=labels,color="black")

    data = go.Sankey(link=link, node=node)
    fig = go.Figure(data)
    title=f"{subject.capitalize()} PI and where they did their Phd"
    fig.update_layout(title_text=title, font_size=10)
    
    return fig
