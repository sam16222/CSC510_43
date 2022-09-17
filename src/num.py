import random
import math
from main import the

class Num:
    def __init__(self,c=0,s=""):
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
    """This function sorts the 'kept' numbers in 'has'.
    It returns the sorted list of numbers"""
    def nums(self):
        if self.isSorted != True:
            self.has.sort()
            self.isSorteed = True
        return self.has
    
    """Reservoir sampler. Keep at most 'the.nums' numbers.
    And if we run out of room, delete something old at random."""
    def add(self,v):
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
    
    """This function calculates the standard deviation for 'nums'.
    It returns the standard deviation or the Diversity"""        
    def div(self):
        """Percentile calculation"""
        def __percentile(lst,n):
            size = len(lst)
            return sorted(lst)[int(math.ceil((size * n) / 100)) - 1]
        
        a = self.nums();
        total = sum(a)
        length = len(a)
        mean = total / length
        std = (sum([((x - mean) ** 2) for x in a]) / length) ** 0.5
        std1 = (__percentile(a,90) - __percentile(a,10))/2.58
        return std1
    
    """This function finds the median for 'nums'.
    It returns the median for the 'nums'"""
    def mid(self):
        lst = self.nums()
        if len(lst)%2==0:
            mid = (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
        else:
            mid = lst[len(lst)//2]
        return mid 

