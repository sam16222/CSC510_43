import unittest
from CSC510_43.src.main import the
from CSC510_43.src.data import Data


class TestData(unittest.TestCase):

    def test_data(n):
        d = Data("data/data1.csv")
        for _, col in enumerate(d.cols.y):
            print(col)
        return True


