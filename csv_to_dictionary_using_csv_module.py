# Your task is to read the input DATAFILE line by line using csv python module
# Using DictReader function

import os
import csv
import pprint


DATADIR = ""
DATAFILE = "beatles-diskography.csv"


def parse_file(DATAFILE):
    data = []
    with open(DATAFILE, "rb") as f:
        d = csv.DictReader(f)
        for line in d:
            data.append(line)
    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    pprint.pprint(d)
    
#    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
#    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
#
#    assert d[0] == firstline
#    assert d[9] == tenthline

    
test()