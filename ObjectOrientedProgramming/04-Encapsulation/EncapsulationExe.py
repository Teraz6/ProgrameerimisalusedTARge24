"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name: str, student_id: int):
        """Set private attributes."""
        self.__name = name
        self.__id = student_id
        self.__status = "Active"

    def get_id(self) -> int:
        """Get student id."""
        return self.__id

    def set_name(self, name: str):
        """Set student name."""
        self.__name = name

    def get_name(self) -> str:
        """Get student name."""
        return self.__name

    def set_status(self, status: str):
        """Set student status."""
        if status in {"Active", "Expelled", "Finished", "Inactive"}:
            self.__status = status

    def get_status(self):
        """Get student status."""
        return self.__status


""" Teine variant seda teha. """
class Student:
    """Represent student with name, id and status."""
    STATUS_ACTIVE = "Active"
    STATUS_EXPELLED = "Expelled"
    STATUS_FINISHED = "Finished"
    STATUS_INACTIVE = "Inactive"
    STATUSES = [STATUS_ACTIVE, STATUS_EXPELLED, STATUS_FINISHED, STATUS_INACTIVE]

    def __init__(self, name: str, student_id: int):
        self.__name = name
        self.__id = student_id
        self.__status = Student.STATUS_ACTIVE