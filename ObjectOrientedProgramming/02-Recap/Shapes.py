"""
Three different shape classes that each calculate the shapes area and circumference.
"""
import math


class Square:
    """Square class."""
    def __init__(self, length):
        """Initialize square instance."""
        self.length = length

    def __repr__(self):
        length = self.length
        return f"Square({length=})"

    def calculate_area(self):
        """Calculate the area of the square."""
        return self.length ** 2

    def calculate_perimeter(self):
        """Calculate the perimeter of the square."""
        return self.length * 4


class Circle:
    """Circle class."""
    def __init__(self, radius):
        """Initialize circle instance."""
        self.radius = radius

    def __repr__(self):
        radius = self.radius
        return f"Circle({radius=})"

    def calculate_area(self):
        """Calculate the area of the circle."""
        return self.radius ** 2 * math.pi

    def calculate_perimeter(self):
        """Calculate the perimeter of the circle."""
        return self.radius * 2 * math.pi


class Triangle:
    """Triangle class. Equal length sides"""
    def __init__(self, a):
        """Initialize triangle instance."""
        self.a = a

    def __repr__(self):
        a = self.a
        return f"Triangle({a=})"

    def calculate_area(self):
        """Calculate the area of the triangle."""
        h = self.a * math.sqrt(3) / 2
        return self.a * h / 2

    def calculate_perimeter(self):
        """Calculate the perimeter of the triangle."""
        return self.a * 3


if __name__ == "__main__":
    square = Square(length=5)
    print(f"{square} area is {square.calculate_area()}")
    print(f"{square} perimeter is {square.calculate_perimeter()}")
    circle = Circle(radius=1)
    print(f"{circle} area is {circle.calculate_area()}")
    print(f"{circle} perimeter is {circle.calculate_perimeter()}")
    triangle = Triangle(3)
    print(f"{triangle} area is {triangle.calculate_area()}")
    print(f"{triangle} perimeter is {triangle.calculate_perimeter()}")