# Research into Israeli Science Community
This is the webapp for my investigation of the Israeli academic science community.

# Description
## What's in the project
There are three sections

1. mobility - where researchers graduated with their PhD and where they got a tenure position
currently only for physics and chemistry.
2. women - women in STEM fields in different institutes 
3. network - network analysis of mobility data, under construction

The project is written in english because streamlit doesn't natively support right-to-left, and I
really don't want to write the website with their HTML api.

## Repository structure
*Folder Structure*
- data/ you will find all relevant data for figure generation
- pages/ strucutre and code for streamlit page generation
- scripts/ scripts used in the pages
- text/ text files for the pages to draw from so that pages won't be too crowded
- in_progress/ pages I'm thinking to add but aren't really active work

# Local install and run
To locally install and run the applet:
1. clone the repository
2. create and activate a virtual environment ```python -m venv venv``` then ```source venv/bin/activate```
3. install requirements: ```pip inatall -r requierments.txt```
4. run the applet ```streamlit run home.py```

And you're good to go.

# Contriubtions
Pull requests are welcome. For major changes, please open an issue first to discus the change you want to make.

Statistical analysis is gathered in the [```data/```](data/) folder, while the code for the webapp is
located at [```pages/```](pages/)


Please make sure to write tests as appropriate, I (Avishai) didn't do the proper and appropriate work so there are currently no tests.

# Author
Contributors names and contact info

Avishai Barnoy [@avishai231](https://twitter.com/avishai231)

# Licesne
This project is licensed under the MIT License - see the LICENSE.md file for details.
