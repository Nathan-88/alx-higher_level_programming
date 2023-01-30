#!/usr/bin/python3
"""defining a class"""


class Square:
    """ square with private instance attribute size"""

    def __init__(self, size=0):
        """i
        Args:
            __size (int): size of side of the square
        """
        self.__size = size
        if isinstance(self.__size, int) is False:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
