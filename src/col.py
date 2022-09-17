from sym import Sym
from num import Num

"""This class "Columns" holds summaries of columns
Columns are created once, then may appear in multiple slots"""
class Cols(object):
    """This constructor assigns the inital values to the variables"""
    def __init__(self, names = []):
        """Assigns default values for all column names,
        all the columns (including skipped ones),
        the single dependent klass column (if it exists),
        independent columns (that are not skipped),
        dependent columns (that are not skipped)
         """
        self.names = names;  
        self.all = []        
        self.klass = None    
        self.x = []          
        self.y = []
        """The for is responsible for identifying the columns and storing them in a list"""
        for idx, name in enumerate(names): 
            """If it starts with an uppercase letter, it's a numeric else a symbol""" 
            col = name[0].isupper() and Num(idx, name) or Sym(idx, name)  
            self.all.append(col)
            """Checks if column needs to be skipped. It is skipped if it ends with ':'."""
            if name[-1] != ':':
                """Checks if column is independent or dependent (that are not skipped). It is a dependent one if it ends in '-' or '+'
                Else it is an independent column"""
                self.y.append(col) if name[-1] == '-' or name[-1] == '+' else self.x.append(col)
                """If it ends in an '!', it's single dependent klass column"""
                if name[-1] == '!':
                    self.klass = col
