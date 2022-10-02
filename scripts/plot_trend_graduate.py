import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path
import streamlit as st

subjects = ["physics", "chemistry", "biology"]
degrees = ["BSc", "MSc", "PhD"]

def get_path(subject, degree): 
    filepath = f"../data/{degree.lower()}_by_year_gender_{subject}.csv"
    path = Path(__file__).parent / filepath
    data = pd.read_csv(path)

    year = data["year"].tolist()
    women = data["women"].tolist()
    men = (data["total"]-data["women"]).tolist()
    return women, men, year

def get_institute(subject, degree, institute):
    filepath = f"../data/{degree.lower()}_by_year_gender_{subject}.csv"
    path = Path(__file__).parent / filepath
    data = pd.read_csv(path)

    year = data["year"].tolist()
    students = data[institute].tolist()
    return students, year

def plot_by_gender(subject, degree, save=False):
    women, men, year = get_path(subject, degree)

    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(8, 6), dpi=90)
        ax.plot(year, men,'o-',markersize=5,label="men")
        ax.plot(year, women,'o-',markersize=5,label="women")
        ax.set_xlabel("year"); ax.set_ylabel("number")
        ax.set_title(f"Number of {degree} graduates in {subject}")
        ax.legend()
        ax.grid(True, lw=0.5, zorder=0)
        plt.ion() 
        if save == True:
            savepath = f"../images/"
            plt.savefig(Path(__file__).parent / f"{savepath}{degree}_{subject}_xkcd.png")
        return fig

def plot_all_degrees_for_subject(subject, degrees, save=False):
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(8, 6), dpi=90)
        for deg in degrees:
            women, men ,year = get_path(subject, deg)
            students = [i+j for i,j in zip(women,men)]
            ax.plot(year, students, "o-", markersize=5, label=deg)
        ax.set_xlabel("year"); ax.set_ylabel("number of graduates")
        ax.set_title(f"Number of graduates in {subject} by degree")
        ax.legend()
        ax.grid(True, lw=0.5, zorder=0)
        plt.ion()
        if save == True:
            savepath = f"../images/"
            plt.savefig(Path(__file__).parent / f"{savepath}all_degrees_{subj}_xkcd.png")
        return fig

def plot_by_institute(institute, subject, save=False):
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(8, 6), dpi=90)
        for deg in degrees:
            students, year = get_institute(subject, deg, institute)
            ax.plot(year, students,'o-',markersize=5,label=deg)
            ax.set_xlabel("year")
            ax.set_ylabel("number of graduates")
            ax.set_title(f"Number of {subject} graduates by degree at the {institute.capitalize()}")
        ax.grid(True, lw=0.5, zorder=0)
        plt.ion()
        ax.legend()
        if save == True:
            savepath = f"../images/"
            plt.savefig(f"bsc_{institute}_chemistry_xkcd.png")
        return fig

def plot_old_data_graduation_all(subject, degrees, save=False):
    filepath = f"../data/combined_data_old.csv"
    path = Path(__file__).parent / filepath
    data = pd.read_csv(path)
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(8, 6), dpi=90)
        year = data["year"].tolist()  
        for deg in degrees:
            grad_number = data[f"{deg.lower()}_{subject}"] 
            ax.plot(year, grad_number, "o-", markersize=5, label=deg)
        ax.set_xlabel("year"); ax.set_ylabel("number of graduates")
        ax.set_title(f"Number of graduates in the {subject} sciences")
        ax.legend()
        ax.grid(True, lw=0.5, zorder=0)
        plt.ion()
        if save == True:
            savepath = f"../images/"
            plt.savefig(Path(__file__).parent / f"{savepath}all_degrees_{subj}_xkcd.png")
        return fig

if __name__ == "__main__":
    pass
    #plot_all_subjects_degrees(subjects, degrees)

