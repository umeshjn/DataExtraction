# Read the input DATAFILE using csv python module
# Write the data into csv file using python csv module reader and writer functions

import os
import csv

DATADIR = ""
INPUTFILE = "beatles-diskography.csv"
OUTPUTFILE = "beatles-diskography_writer.csv"

def read_file(DATAFILE):
    with open(DATAFILE, "rb") as f:
        d = csv.reader(f)
        writeinto = csv.writer(open(OUTPUTFILE,"wb"),delimiter=',')
        for line in d:
            writeinto.writerow(line)

def test():
    datafile = os.path.join(DATADIR, INPUTFILE)
    read_file(datafile)
    
test()