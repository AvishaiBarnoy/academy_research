import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path


subject = "chemistry"
#subject = "physics"

degree = "MSc"
#degree = "PhD"

path = f"../data/{degree.lower()}_by_year_gender_{subject}.csv"
data = pd.read_csv(path)#, index_col=0)

year = data["year"].tolist()
women = data["women"].tolist()
men = (data["men"]-data["women"]).tolist() 

with plt.xkcd():
    fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
    ax.plot(year, men,'o-',markersize=5,label="men")
    ax.plot(year, women,'o-',markersize=5,label="women")
    ax.set_xlabel("year")
    ax.set_ylabel("number")
    ax.set_title(f"Number of {degree} graduates in {subject}")
    ax.legend()
    plt.savefig(f"{degree}_{subject}_xkcd.png")
