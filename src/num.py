import random
from CSC510_43.src.main import the

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
    
    def nums(self):
        if self.isSorted != True:
            self.has.sort()
            self.isSorteed = True
        return self.has
    
    def add(self,v):
        if v!="?":
            self.n = self.n+1
            self.lo = min(v, self.lo)
            self.hi - max(v, self.hi)
        length = len(self.has) 
        if length < the['nums']:
            pos = length
        elif random.random() < the['nums'] / self.n:
            pos = random.randint(0,length-1)
        if pos>=0:
            self.isSorted = False
            if length < the['nums']:
                self.has.append(float(v))
            else: 
                self.has[pos]=float(v)
            
    def div(self):
        a = self.nums();
        total = sum(a)
        length = len(a)
        mean = total / length
        std = (sum([((x - mean) ** 2) for x in a]) / length) ** 0.5
        return std
    
    def mid(self):
        lst = self.nums()
        if len(lst)%2==0:
            mid = (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
        else:
            mid = lst[len(lst)//2]
        return mid 