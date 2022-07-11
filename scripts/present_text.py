import streamlit as st
from pathlib import Path


def text_intro_subject(subject):
    with open(f"text/{subject.lower()}_sankey.txt") as f:
        phys_txt = ''.join(f.readlines())
    st.write(phys_txt)

def text_sankey_analysis(subject):
    with open(f"text/{subject.lower()}_analysis.txt") as f:
        phys_txt = ''.join(f.readlines())
    st.write(phys_txt)

