from abc import ABC, abstractmethod
class Brand:
    @abstractmethod
    def __init__(self, info):
        self.V = info
        self.sum = 0
    @abstractmethod
    def findspace(self):
        self.sum += self.V
class Coat(Brand):
    def __init__(self, V):
        self.sum = 0
        self.V = V
    @property
    def findspace(self):
        self.sum += self.V/6.5 + 0.5
        return self.sum
class Suit(Brand):
    def __init__(self, H):
        self.sum = 0
        self.H = H
    @property
    def findspace(self):
        self.sum += self.H * 2 + 0.3
        return self.sum
suit1 = Suit(13)
print(suit1.findspace)
coat1 = Coat(13)
print(coat1.findspace)