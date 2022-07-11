# Research into Israeli Science Community
This is the webapp for my investigation of the Israeli academic science community.

# Description
## What's in the project
Currently only where professors studied and where they got their tenure position, and
only for physics. In the future it will include data for the chemistry departments.

Another future project is to analyze a lot of data I have about gender PI's, undergraduate
and graduate in STEM.

The project is written in english because streamlit doesn't support right-to-left natively, and I
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
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Also, don't forget to update the changes in the [`CHANGELOG.md`](./CHANGELOG.md) file.

Statistical analysis is gathered in the ```data/``` folder, while the code for the webapp is located at ```pages/```


Please make sure to write tests as appropriate, I (Avishai) didn't do the proper and appropriate work so there are currently no tests.


# Author
Contributors names and contact info

Avishai Barnoy [@avishai231](https://twitter.com/avishai231)

# Licesne
This project is licensed under the MIT License - see the LICENSE.md file for details.
