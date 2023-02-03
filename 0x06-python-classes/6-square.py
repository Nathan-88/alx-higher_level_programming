#!/usr/bin/python3


class Square:
    """ defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """initializer for sqaure
        Args:
            size: size of square
            position: position of square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter for size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        Args:
            value (int): size of side of square
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i > 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ area of the square
        Returns:
            square of size
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__position):
                print(" ", end="")
            for k in range(self.__size):
                print("#", end="")
            print("")
