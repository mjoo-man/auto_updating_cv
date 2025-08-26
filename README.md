# Auto-Updating CV
This repository is my attempt to automate updating the publications portion of my CV with a python web scraper and github actions. 

# To use
1. Edit the `scripts/get_citations.py` with your google scholar ID and your name if you would like is to bold you name in the author lists.

2. run `get_citations.py` using your favorite python method then push the bib files to the repo. 

3. gh actions will build your updated pdf in a few minutes. pull or download from there. 

# How it works
1. The python script will query my Google Scholar page using a unique ID (found in the scholar profile URL). It will then generate a list of Journal Articles an Conference Proceedings in respective `.bib` files.
   
   The script assigns `@inprocedings` bibtex markers to conference papers and `@article` markers to journal papers. Presented abstracts are not tracked on scholar so they were done manually with `@misc`.

**TODO: Google scholar will reject the query from Github Actions server. for now it can be run locally with the `.bib` files committed and pushed to the repo. Eventually this will be done automatically with gh actions**
```sh
# run locally to generate a list of publications
source env/bin/activate
python3 scripts/get_citations.py
```

2. The updated `.bib` files are imported into the `cv.tex` and sorted accordingly using the `type` command in the bibliography.
   ```tex
   \section{Journal Articles}
   \nocite{*} % cite a without a reference number
    
    \printbibliography[
    heading=none,
    type=article % or inproceedings or misc depending on the section targeted
    ]
   ```
3. GitHub will compile the LaTeX code on pushes to and `.tex` or `.bib` file and upload the final pdf
