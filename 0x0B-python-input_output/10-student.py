#!/usr/bin/python3
"""a class Student that defines
a student by: (based on 9-student.py)
"""


class Student():
    """defines a class of student
    """
    def __init__(self, first_name, last_name, age):
        """define instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            diction = {}
            if isinstance(attrs, list):
                if all(isinstance(attr, str) for attr in attrs):
                    for i in attrs:
                        if i in self.__dict__:
                            diction.update({i: self.__dict__[i]})
            return diction
