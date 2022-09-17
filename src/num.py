import random
import math
from main import the

class Num:
    """'Num' summarizes a stream of numbers"""
    def __init__(self,c=0,s=""):
        """The constructor assigns the inital values to the variables
        n, at, name and has as per Sym,
        lo (lowest seen) to positive infinity,
        hi (highest seen) to negative infinity
        isSorted (to see if it's sorted and check for
        any updates since last sort of data) to 'True'"""
        self.n = 0
        self.at = c
        self.name = s
        self.has = []
        self.lo = float('inf')
        self.hi = float('-inf')     
        self.isSorted = True
        if self.name!="" and self.name[-1]=='-':
            self.w = -1
        else:
            self.w = 1

    def nums(self):
        """This function sorts the 'kept' numbers in 'has'.
        It returns the sorted list of numbers"""
        if self.isSorted != True:
            self.has.sort()
            self.isSorteed = True
        return self.has
    
    def add(self,v):
        """Reservoir sampler. Keep at most 'the.nums' numbers.
        And if we run out of room, delete something old at random."""
        if v!="?":
            self.n = self.n+1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
        length = len(self.has) 
        pos = -1
        if length < the['nums']:
            pos = length
        elif random.random() < the['nums'] / self.n:
            pos = random.randint(0,length-1)
        if pos >= 0:
            self.isSorted = False
            if length < the['nums']:
                self.has.append(float(v))
            else: 
                self.has[pos]=float(v)
    
       
    def div(self):
        """This function calculates the standard deviation for 'nums'.
        It returns the standard deviation or the Diversity""" 
        
        def __percentile(lst,n):
            """Percentile calculation"""
            size = len(lst)
            return sorted(lst)[int(math.ceil((size * n) / 100)) - 1]
        
        a = self.nums();
        total = sum(a)
        length = len(a)
        mean = total / length
        std = (sum([((x - mean) ** 2) for x in a]) / length) ** 0.5
        std1 = (__percentile(a,90) - __percentile(a,10))/2.58
        return std1
    
    def mid(self):
        """This function finds the median for 'nums'.
        It returns the median for the 'nums'"""
        lst = self.nums()
        if len(lst)%2==0:
            mid = (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
        else:
            mid = lst[len(lst)//2]
        return mid 

