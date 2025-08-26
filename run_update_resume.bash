#!/bin/bash

source env/bin/activate
python3 scripts/get_citations.py
deactivate # the venv

# build pdf
latexmk -pdfxe cv.tex
# clean extra files from complile
latexmk -c
rm cv.bbl # remove extra biber file