#!/usr/bin/python3
"""defines a class, square"""


class Square:
    """ Represent square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): the size of square
        """
        self.size = size

    @property
    def size(self):
        """getter for size of square

        Returns:
            the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter

        Args:
            value (int):new size of square
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returns current square area"""
        return (self.__size) ** 2
