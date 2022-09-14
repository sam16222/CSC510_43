from main import the
from data import Data

def test_data():
    d = Data("../data/data1.csv")
    for _, col in enumerate(d.cols.y):
        print(col.name)
    return 0


