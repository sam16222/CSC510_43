import numbers


from abc import ABCMeta, abstractmethod

class VariableInterface:
    __metaclass__ = ABCMeta


    @abstractmethod
    def add(self, val): raise NotImplementedError
    @abstractmethod
    def mid(self): raise NotImplementedError
    @abstractmethod
    def div(self): raise NotImplementedError