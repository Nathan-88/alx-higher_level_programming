#!/usr/bin/python3
"""defines a class, square"""

class Square:
    """ class square"""
    def __init__(self, size=0):
        """initializer of class square
        Args:
            __size: size of square
        """
        self.__size = size

    @property
    def size(self):
        """getter for size of square
        Returns: private instance
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter
        Args:
            value(int):new size of square
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be a integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns current square area"""
        return self.__size ** 2
