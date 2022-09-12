import unittest
from CSC510_43.src.data import Data


class TestStats(unittest.TestCase):

    def test_stats(n):
        data = Data("data/data1.csv")
        print('xmid=', data.stats(2, data.cols.x, "mid"))
        print('xdiv=', data.stats(3, data.cols.x, "div"))
        print('ymid=', data.stats(2, data.cols.y, "mid"))
        print('ymid=', data.stats(3, data.cols.y, "div"))
        return True


if __name__ == "__main__":
    unittest.main()
