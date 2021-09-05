from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption


class Coat(Clothes):

    @property
    def fabric_consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):

    @property
    def fabric_consumption(self):
        return (2 * self.param + 0.3) / 100


coat = Coat(44)
costume = Costume(170)
print(coat + costume)
