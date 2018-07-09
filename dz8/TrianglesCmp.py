from math import sqrt
from itertools import permutations

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
        self.empty = False if a<b+c and b<a+c and c<a+b and a>0 and b>0 and c>0 else True

    def __str__(self):
        return "{:.1f}:{:.1f}:{:.1f}".format(self.a, self.b, self.c)

    def __bool__(self):
        return not self.empty

    def __abs__(self):
        if self.empty:
            return 0
        p = (self.a + self.b + self.c) / 2
        return sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def __eq__(self, other):
        return (self.a, self.b, self.c) in permutations([other.a, other.b, other.c])

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)