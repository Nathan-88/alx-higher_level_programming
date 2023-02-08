#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry():
    """defines class"""

    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if not isinstance(name, str):
            raise Exception()
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.name = name
        self.value = value

