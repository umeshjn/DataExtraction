# Read the input csv file and print read row by splitting on comma.

import os


DATADIR = ""
DATAFILE = "beatles-diskography_modified.csv"


def read_file(DATAFILE):
    with open(DATAFILE, "rb") as f:
        for line in f:
            fields = line.split(',')
            print fields

def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    read_file(datafile)
   
    
test()