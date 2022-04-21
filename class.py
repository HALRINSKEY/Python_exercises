
import math
"""
class Circle():
    def __init__(self,d):
        self.diameter = d
    def area(self):
        return (self.diameter / 2) ** 2 * math.pi

d = int(input())
c = Circle(d)
print(c.area())
"""

class Triangle:
    def __init__(self,s,h):
        self.side = s
        self.heght = h

    def area(self):
        return (self.side * self.heght) / 2

t = Triangle(2,2)
print(t.area())
