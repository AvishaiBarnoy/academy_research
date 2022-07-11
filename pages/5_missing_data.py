import streamlit as st
import pandas as pd
from pathlib import Path

st.markdown(
    """
    # Under Construction
    # Missing Data
    Here is a list of professors that I was not able to find where they studied for their PhD.
    ## Physics
    """)

miss_phys_path = Path(__file__).parent / "../data/physics_missing.csv"
miss_phys = pd.read_csv(miss_phys_path).fillna("")
st.table(miss_phys)

st.markdown("""
    ## Chemistry
    """)

miss_chem_path = Path(__file__).parent / "../data/chemistry_missing.csv"
miss_chem = pd.read_csv(miss_chem_path).fillna("")
st.table(miss_chem)
