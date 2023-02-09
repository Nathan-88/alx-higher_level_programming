#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)"""


class BaseGeometry():
    """defines class"""

    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """represents a rectangle"""

    def __init__(self, width, height):
        """initializer for rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
