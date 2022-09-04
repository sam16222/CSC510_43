import unittest
from CSC510_43.src.sym import Sym

class TestSym(unittest.TestCase):

    def test_div(self):
        '''Test case for div function'''
        arr = ["a", "a", "a", "a", "b", "b", "c"]
        sym = Sym(object)
        for index, value in enumerate(arr):
            sym.add(value)
        entropy = sym.div()
        entropy = (1000*entropy)//1/1000
        self.assertTrue(1.37 <= entropy <= 1.38)

    def test_mid(self):
        '''Test case for mid function'''
        arr = ["a", "a", "a", "a", "b", "b", "c"]
        sym = Sym(object)
        for index, value in enumerate(arr):
            sym.add(value)
        mode = sym.mid()
        expected = "a"
        self.assertEqual(mode, expected)

if __name__ == "__main__":
  unittest.main()


