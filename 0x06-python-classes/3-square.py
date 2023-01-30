#!/usr/bin/python3
"""defines a square"""


class Square:
    """square with private instance"""
    def __init__(self, size=0):
        """initializes a square
        Args:
            __self (int): A private instance attribute
        """
        self.__size = size
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """public instance method
        Return:
            square Area
        """
        return self.__size ** 2
