import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import numpy as np

subjects = ["physics", "chemistry"]
degrees = ["BSc", "MSc", "PhD"]

def get_path(subject, degree): 
    filepath = f"../data/{degree.lower()}_by_year_gender_{subject}.csv"
    path = Path(__file__).parent / filepath
    data = pd.read_csv(path)

    year = data["year"].tolist()
    women = data["women"].tolist()
    men = (data["men"]-data["women"]).tolist()

    return women, men, year

def plot_xkcd(subject, degree):
    women, men ,year = get_path(subject, degree)

    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
        ax.plot(year, men,'o-',markersize=5,label="men")
        ax.plot(year, women,'o-',markersize=5,label="women")
        ax.set_xlabel("year")
        ax.set_ylabel("number")
        ax.set_title(f"Number of {degree} graduates in {subject}")
        ax.legend()

        savepath = f"../images/"
        plt.savefig(Path(__file__).parent / f"{savepath}{degree}_{subject}_xkcd.png")

def plot_all_subjects_degrees(subjects, degrees):
    for subj in subjects:
        with plt.xkcd():
            fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
            for deg in degrees:
                women, men ,year = get_path(subj, deg)
                students = [i+j for i,j in zip(women,men)]
                ax.plot(year, students, "o-", markersize=5, label=deg)
                #ax.plot(year, men,'o-',markersize=5,label="men")
                #ax.plot(year, women,'o-',markersize=5,label="women")
            ax.set_xlabel("year"); ax.set_ylabel("number of students")
            ax.set_title(f"Number of students in {subj} by degree")
            ax.legend()

            savepath = f"../images/"
            plt.savefig(Path(__file__).parent / f"{savepath}all_degrees_{subj}_xkcd.png")

def plot_institute():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
        ax.plot(data["year"].tolist(), data["students"].tolist(),'o-',markersize=5,label="bsc")
        ax.set_xlabel("year")
        ax.set_ylabel("number of students")
        ax.set_title(f"Number of chemistry bachelors in the Technion")
        ax.legend()
        plt.savefig(f"bsc_technion_chemistry_xkcd.png")


if __name__ == "__main__":
    pass
    #plot_all_subjects_degrees(subjects, degrees)

