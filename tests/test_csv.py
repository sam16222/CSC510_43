from main import the
from misc import csv
from row import Row
n = 0
def test_csv():
    '''Test case for csv'''
    def _fn(row):
        global n
        n += 1
        if(n>10):
            return
        else:
            print(row)
    csv("../data/data1.csv", _fn)
    return 0

            

