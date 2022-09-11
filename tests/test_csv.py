import unittest
from CSC510_43.src.misc import csv
from CSC510_43.src.row import Row


class TestCSV(unittest.TestCase):
    n = 0
    def fn(self,row):
        self.n = self.n + 1
        if(self.n>10):
            return
        else:
            print(row)

    def test_csv(self):
        csv("../data/data1.csv", self.fn)
        return True

            

