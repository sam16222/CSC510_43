from main import the
from num import Num

def test_num():
    '''Test case for div function'''
    num = Num()
    the['nums'] = 512
    for i in range(1, 101):
        num.add(i)
    std = num.div()
    median = num.mid()
    return 0 if 30 < std < 32 and 50 <= median <= 52 else 1