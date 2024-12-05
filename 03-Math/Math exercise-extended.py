"""Math exercises vol2."""
import math


def time_converter(seconds: int) -> str:
    """Convert time in seconds to hours and minutes."""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{seconds} sekundit on {hours} tund(i) ja {minutes} minut(it)."


def student_helper(angle: int) -> str:
    """Return the sine and cosine of the given angle in degrees."""
    rad = math.radians(angle)
    sine = math.sin(rad)
    cosine = math.cos(rad)
    return f"Nurk: {angle}, siinus: {sine:.1f}, koosinus: {cosine:.1f}."


def greetings(n: int) -> str:
    """Return a string that contains "Hey" n times."""
    lots_of_heys = "Hey" * n
    return lots_of_heys


def adding_numbers(num_a: int, num_b: int) -> str:
    """Return given numbers added together as a string"""
    string_numbers = f"{num_a}{num_b}"
    return string_numbers


if __name__ == "__main__":
    assert time_converter(7600) == (f"{7600} sekundit on {2} tund(i) ja {6} minut(it).")
    assert time_converter(13526) == (f"{13526} sekundit on {3} tund(i) ja {45} minut(it).")

    assert student_helper(45) == (f"Nurk: {45}, siinus: {0.7}, koosinus: {0.7}.")
    assert student_helper(74) == (f"Nurk: {74}, siinus: {1.0}, koosinus: {0.3}.")

    assert greetings(3) == ("Hey" "Hey" "Hey")
    assert greetings(14) == ("Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey" "Hey")

    assert adding_numbers(5, 2) == ("52")
    assert adding_numbers(19, 34) == ("1934")
    print("Korras")