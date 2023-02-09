#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ represents a subclass square"""

    def __init__(self, size):
        """initializer for square"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """area of square"""
        return self.__size ** 2

    def __str__(self):
        """print"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
