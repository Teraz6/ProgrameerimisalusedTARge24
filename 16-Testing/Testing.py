import math

def solve_quadratic_equations(a, b, c):
    """
    Solving quadratic quation
    ax^2 + bx + c = 0
    :param a:
    :param b:
    :param c:
    :return: (x1, x2) tuple
    """
    disc = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(disc)) / (2 * a)
    x2 = (-b - math.sqrt(disc)) / (2 * a)
    return x1, x2

def test__solve_quadratic_equations__two_solutions():
    assert solve_quadratic_equations(2, 6, 20) == (-5.0, 2.0)

def test__solve_quadratic_equations__two_float_solutions():
    x1, x2 = solve_quadratic_equations(2, 3, -57)
    assert (round(x1,3), round(x2,3)) == (-6.141, 4.641)