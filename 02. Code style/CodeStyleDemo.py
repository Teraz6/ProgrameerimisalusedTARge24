"""Demonstrate how codestyle should be applied"""


def output_int_value_of(a):
    """
    Third function
    :param a: integer string that should be printed
    """
    print(int(a))  # Attempt to convert string <The output is called 'Stack Trace'> to int and print it out

def combine(a, b):
    """
    add two parameters together.

    :param a: first value to add
    :param b: second value to add
    """
    c = a + b
    print(c)  # --> The output is called 'Stack Trace'

    # Calling the third function
    output_int_value_of(c)


def start_program():
    """Start """
    # Calling the second function
    combine("The output is called ", "'Stack Trace'")

start_program()