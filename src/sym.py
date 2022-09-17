import math

"""Sym's summarize a stream of symbols"""
class Sym(object):
    def __init__(self, at = 0, name = ""):
        """The constructor assigns the inital values to the variables
        number of items seen 'n',
        column position 'c',
        column name 'name',
        and data kept 'has'."""
        self.at = at
        self.name = name
        self.n = 0
        self.has = {}
    """Add one thing to 'col'. 
    For Numerics we can keep at most 'nums' items"""
    def add(self, val):
        if val != "?":
            if val in self.has: 
                self.has[val] += 1
            else:
                
                self.has[val] = 1
            self.n += 1
    
    """This function finds the mode for items in 'has'.
    It takes the column as an input and returns the mode as the output"""
    def mid(self):
        most = -1
        for key, value in self.has.items():
            if value > most:
                most = value
                mode = key
        return mode
    """This function finds the entropy for items in 'has'.
    It returns the entropy as the output"""
    def div(self):
        def __fun(p):
            return p*math.log2(p)
        e = 0
        for _, value in self.has.items():
            if value > 0:
                e -= __fun(value/self.n)
        return e