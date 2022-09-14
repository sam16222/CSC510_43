import sys
sys.path.insert(0, '../src')
from main import the

def test_the():
    '''Test case for the'''
    try:
        the
    except NameError:
        return 1
    else:
        return 0

