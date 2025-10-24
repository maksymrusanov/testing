import math
from email.headerregistry import ContentTypeHeader


class Shape:
    def area(self):
        pass

    def perimetr(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimetr(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.width == other.width and self.length == other.length

    def area(self):
        return self.width * self.length

    def perimetr(self):
        return (self.length * 2) + (self.width * 2)


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
