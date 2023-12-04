from math import pow
from numbers import Number
from random import randrange


class Calculator:

    def __init__(self, x: Number, y: Number):
        self.x = x
        self.y = y

    def plus(self):
        return self.x + self.y

    def minus(self):
        return self.x - self.y

    def divide(self):
        return self.x / self.y

    def multiply(self):
        return self.x * self.y

    def pow(self):
        return pow(self.x, self.y)

    @staticmethod
    def random(a: int, b: int):
        return randrange(a, b)
