import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

def shapes(shapes):
    print(shapes.area())
circle=Circle(5)
rectangle=Rectangle(5,7)
shapes(circle)
shapes(rectangle)
