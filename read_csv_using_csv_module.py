# Read the input DATAFILE line by line using csv python module

import os
import csv

DATADIR = ""
INPUTFILE = "beatles-diskography.csv"
OUTPUTFILE = "beatles-diskography_written.csv"

def read_file(DATAFILE):
    with open(DATAFILE, "r") as f:
        d = csv.reader(f)
        for line in d:
            print line

def test():
    datafile = os.path.join(DATADIR, INPUTFILE)
    read_file(datafile)

    
test()