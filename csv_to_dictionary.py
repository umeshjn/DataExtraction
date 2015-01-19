# Read the input csv file 
# form the dictionary using the header values as the keys and other rows values as its values.

import os
import pprint


DATADIR = ""
DATAFILE = "beatles-diskography_modified.csv"


def parse_file(DATAFILE):
    data = []
    with open(DATAFILE, "r") as f:
        header = f.readline().split(',')

        for line in f:
            fields = line.split(',')
            entry = {}
            
            for i,value in enumerate(fields):
                entry[header[i].strip()]=value.strip()
            data.append(entry)

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    pprint.pprint(d)
    
    
test()