from data import Data

def test_stats():
    print()
    print("Test case for stats")
    data = Data("../data/data1.csv")
    print('xmid=', data.stats(2, data.cols.x, "mid"))
    print('xdiv=', data.stats(3, data.cols.x, "div"))
    print('ymid=', data.stats(2, data.cols.y, "mid"))
    print('ymid=', data.stats(3, data.cols.y, "div"))
    print()
    return 0
