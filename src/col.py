from CSC510_43.src.sym import Sym
from CSC510_43.src.num import Num

class Cols(object):
    def __init__(self, names = []):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for idx, name in enumerate(names):
            col = name[0].isupper() and Num(idx, name) or Sym(idx, name)
            self.all.append(col)
            if not name[-1] == ':':
                self.y.append(col) if name[-1] == '-' else self.x.append(col)
                if name[-1] == '!':
                    self.klass = col
