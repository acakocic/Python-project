import sys
import csv
from main import *

def make_excel(out_file):  
    with open(out_file, mode='wt', newline='') as out_file:
        w = csv.writer(out_file) #,delimiter=',')
        for x in children_list:
            col1 = x.first_name
            col2 = x.last_name
            col3 = x.age()
            col4 = x.gender
            col5 = x.address
            col6 = x.trustee_list[0].first_name
            col7 = x.trustee_list[0].last_name
            col8 = x.trustee_list[0].phone
            line = [col1, col2, col3, col4, col5, col6, col7, col8]
            w.writerow(line)

if __name__ == "__main__":
    out_file = sys.argv[1]
    result = make_excel(out_file)