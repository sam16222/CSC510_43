import copy

"""The class 'Row' holds one record"""
class Row:
    def __init__(self,t):
        """This constructor assigns the corresponding values to the variables: 
            cells       -   record being passed, 
            cooked      -   used if we discretize data,
            isEvaled    -   true if y-values are evaluated
        """
        self.cells = t
        self.cooked = copy.copy(t)
        self.isEvaled = False
