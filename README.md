# Auto-Updating CV

Its a pain to keep updating the current publications for an academic CV. This repository is my attempt to automate the process with a python web scraper and github actions. 

# State of the project
The python script can query my Google Scholar page sing my unique ID. It will then generate a list of Journal Articles an Conference Proceedings in respective `.bib` files. It has to be run locally, google scholar will reject the query from Github Actions server.

```sh
# run to generate a list of publications
source env/bin/activate
python3 scripts/get_citations.py
```

# extra packages installed
```sh
# because I couldnt find the biblatex.sty
sudo apt update
sudo apt install texlive-bibtex-extra biber

```