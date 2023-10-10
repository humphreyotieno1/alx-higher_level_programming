#!/usr/bin/python3
"""Define a class called Student"""


class Student:
    """Represent a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize new Student
        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int):age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dictionary rep of the Student.
        Args:
            attrs (list): attributes to represent
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {(k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
