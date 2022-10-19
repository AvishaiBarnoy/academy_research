import streamlit as st
import pandas as pd

def nopa(filepath):
    """
    nepotism index - nopa
    r_ii ::: phd at i hired by i
    h_i ::: all hired that did phd in i
    returns r_ii/h_i
    """
    pand = pd.read_csv(filepath,delimiter='\t',index_col=0)
    cols = pand.columns.tolist()
    nopa_list = []
    for i,j in enumerate(cols):
        row_i = pand.iloc[i]
        sum_i = sum(row_i)
        inst = cols[i]
        if sum_i != 0:
            nopa = row_i[i]/sum_i
        else:
            nopa = 0
        nopa_list.append((inst,nopa))
    #nopa_df = pd.DataFrame() 
    return nopa_list

if __name__ == "__main__":
    from pathlib import Path
    import numpy as np
    path = f"../data/physics_data.txt"
    nopa = nopa(Path(__file__).parent / path)
    #print(nopa)
    print(np.array(nopa))
    #print(pd.DataFrame(nopa))
