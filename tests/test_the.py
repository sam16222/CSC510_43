import unittest
from CSC510_43.src.main import the

class TestNum(unittest.TestCase):

    def test_the(self):
        '''Test case for the'''
        try:
            the
        except NameError:
            exists = False
        else:
            exists = True
        self.assertTrue(exists)
        self.assertTrue(len(the) == 6)

if __name__ == "__main__":
  unittest.main()


