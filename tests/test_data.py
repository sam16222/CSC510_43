from main import the
from data import Data

def test_data():
    print("Test case for data")
    d = Data("../data/data1.csv")
    for _, col in enumerate(d.cols.y):
        print(col.name)
    print()
    return 0 if len(d.cols.y) == 3 else 1


