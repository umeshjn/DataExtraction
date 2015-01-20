#Code to read the xls file using xlrd python module. 
#And also do the manipulation of the data for extracting the details of the data in specific col

import xlrd
import pprint 


datafile = "2014_ERCOT_Hourly_Load_Data.xls"


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
       
    coast = sheet.col_values(1,start_rowx=1,end_rowx=None)
    
    maxvalue = max(coast)
    minvalue = min(coast)
    
    
    maxposition = coast.index(maxvalue) + 1
    minposition = coast.index(minvalue) + 1
    
    maxdate = sheet.cell_value(maxposition,0)
    maxdate = xlrd.xldate_as_tuple(maxdate,0)
    mindate = sheet.cell_value(minposition,0)
    mindate = xlrd.xldate_as_tuple(mindate,0)
    avgcoast = sum(coast) /float(len(coast))
    
    data = {
            'maxtime' : maxdate,
            'maxvalue' : maxvalue,
            'mintime' :mindate,
            'minvalue' : minvalue,
            'avgcoast' : avgcoast
    }
    
    return data

def test():
    data = parse_file(datafile)
    pprint.pprint(data)


test()
