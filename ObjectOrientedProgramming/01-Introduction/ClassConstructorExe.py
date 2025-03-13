"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        """TODO: Understand how this works."""
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        """TODO: docstring."""
        self.firstname = firstname
        self.lastname = lastname
        self.age = age


if __name__ == '__main__':
    empty = Empty()
    person = Person()
    student = Student(firstname="John", lastname="Smith", age=25)
    print(student)
    student = Student(firstname="Calix", lastname="Sangal", age=22)
    print(student)
    student = Student(firstname="Teemu", lastname="Zhina", age=2)
    print(student)