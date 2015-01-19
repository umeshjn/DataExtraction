# Read the input DATAFILE using csv python module
# Write the data into csv file using python module Dictreader and DictWriter functions

import os
import csv

DATADIR = ""
INPUTFILE = "beatles-diskography.csv"
OUTPUTFILE = "beatles-diskography_dictwriter.csv"

def read_file(DATAFILE):
    with open(DATAFILE, "rb") as f:
        fieldnames = ['Title','Released','Label','UK Chart Position','US Chart Position','BPI Certification','RIAA Certification']
        d = csv.DictReader(f)
        writeinto = csv.DictWriter(open(OUTPUTFILE,"wb"),delimiter=',',fieldnames=fieldnames)
        for line in d:
            writeinto.writerow(line)

def test():
    datafile = os.path.join(DATADIR, INPUTFILE)
    read_file(datafile)
    
test()