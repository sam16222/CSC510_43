import unittest
from CSC510_43.src.num import Num

class TestNum(unittest.TestCase):

    def test_mid(self):
        '''Test case for mid function'''
        num = Num()
        for i in range(1, 101):
            num.add(i)
        mode = num.mid()
        self.assertTrue(50 <= mode <= 52)

    
    def test_div(self):
        '''Test case for div function'''
        num = Num()
        for i in range(1, 101):
            num.add(i)
        entropy = num.div()
        self.assertTrue(28 < entropy < 30)

if __name__ == "__main__":
  unittest.main()


