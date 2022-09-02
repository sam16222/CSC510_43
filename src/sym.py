import math

class Sym(object):
    def __init__(self, at = 0, name = ""):
        self.at = at
        self.name = name
        self.n = 0
        self.has = {}
    def add(self, val):
        if val != "?":
            if val in self.has: 
                self.has[val] += 1
            else:
                
                self.has[val] = 1
            self.n += 1
    
    def mid(self):
        most = -1
        for key, value in self.has.items():
            if value > most:
                most = value
                mode = key
        return mode

    def div(self):
        def __fun(p):
            return p*math.log2(p)
        e = 0
        for _, value in self.has.items():
            if value > 0:
                e -= __fun(value/self.n)
        return e