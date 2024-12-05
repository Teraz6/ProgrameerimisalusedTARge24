"""math exercise."""
import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    summa = num_a + num_b
    difference = num_a - num_b
    return summa, difference


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    # Write your code here
    return num_a / num_b


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    # Write your code here
    return num_a // num_b


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    # Write your code here
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    return (num_a + num_b) / 2


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = radius ** 2 * math.pi
    return round(circle_area, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = math.sqrt(3) / 4 * side_length ** 2
    return round(triangle_area)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = b ** 2 - 4 * a * c
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = math.sqrt(a ** 2 + b ** 2)
    return round(c, 2)


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = math.sqrt(c ** 2 - a ** 2)
    return round(b, 2)

"""See on testimis kood"""
if __name__ == '__main__':
    assert sum_and_difference(5, 6) == (11, -1)
    assert sum_and_difference(11, 9) == (20, 2)

    assert float_division(10, 5) == (2)
    assert float_division(5, 10) == (0.5)

    assert integer_division(5, 8) == (0)
    assert integer_division(22, 2) == (11)
    assert integer_division(22, 4) == (5)

    assert powerful_operations(5, 6) == (30, 15625, 5)
    assert powerful_operations(11, 2) == (22, 121, 1)

    assert find_average(15, 7) == (11)
    assert find_average(12, 9) == (10.5)

    assert area_of_a_circle(4) == (50.27)
    assert area_of_a_circle(7) == (153.94)

    assert area_of_an_equilateral_triangle(4) == (7)
    assert area_of_an_equilateral_triangle(8) == (28)

    assert calculate_discriminant(5, 6, 4) == (-44)
    assert calculate_discriminant(11, 28, 8) == (432)

    assert calculate_hypotenuse_length(15, 15) == (21.21)
    assert calculate_hypotenuse_length(3, 28) == (28.16)

    assert calculate_cathetus_length(9, 15) == (12)
    assert calculate_cathetus_length(5, 26) == (25.51)
    print("Korras")