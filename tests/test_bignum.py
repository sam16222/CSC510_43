from main import the
from num import Num

def test_bignum():
    '''Test case for storage'''
    num = Num()
    the['nums'] = 32
    for i in range(1, 1001):
        num.add(i)
    return 0 if len(num.has) == 32 else 1


