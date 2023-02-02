#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """defines a rectangle"""

    def __init__(self, width=0, height=0):
        """initializes a rectangle
        Args:
            width: width of the rectangle
            height: heigth of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the private instance width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for private instance width"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for private instance height"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """a public instance method of rectangle
        Returns: area of a rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """public method
        Returns: perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """defines string representation of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join('#' * self.__width for i in range(self.__height))

    def __repr__(self):
        """defines an unambigious string representation of an object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
