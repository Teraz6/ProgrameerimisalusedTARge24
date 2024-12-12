"""Function examples."""


# func()
def func():
    """Print to console - I´m inside the function."""
    print("I´m inside the function")

# my_name_is(name)
def my_name_is(name:str) -> None:
    """
    Print to console. - My name is [name].

    :param name: name you want to use
    """
    print(f"My name is {name}")


# sum_six(num)`
def sum_six(num:int) -> int:
    """
    Add six to given number

    :param num: number you want to add
    :return: sum of six
    :type num: object
    """
    return 6 + num


# sum_numbers()
def sum_number(a:int, b:int):
    """
    Add number to given number

    :param a: first number
    :param b: second number
    :return: sum of number a and b
    """
    return a + b


# usd_to_eur
def usd_to_eur(a:int) -> float:
    """

    :param a: Dollar amount
    :return: Euro amount
    """
    return a * 0.8


if __name__ == "__main__":
    func()
    my_name_is("Reten")
    my_name_is("Kalle")
    print(sum_six(4))
    print(sum_six(21))
    print(sum_six(-5))
    print(sum_number(2,3))
    print(sum_number(17,8))
    print(usd_to_eur(2))
    print(usd_to_eur(17))