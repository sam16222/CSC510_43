from sym import Sym

def test_sym():
    '''Test case for div function'''
    arr = ["a", "a", "a", "a", "b", "b", "c"]
    sym = Sym()
    for index, value in enumerate(arr):
        sym.add(value)
    entropy = sym.div()
    entropy = (1000*entropy)//1/1000
    mode = sym.mid()
    return 0 if 1.37 <= entropy <= 1.38 and mode == "a" else 1

