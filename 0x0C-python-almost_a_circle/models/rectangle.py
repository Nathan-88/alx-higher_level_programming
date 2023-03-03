#!/usr/bin/python3
"""he class Rectangle that
inherits from Base:
"""
from models.base import Base


class Rectangle(Base):
    """defines a class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the private attr of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieves the private attr of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieves the private attr of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """assign initialised argument to the right attributea value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area value of rectangle"""
        return self.__width * self.__height

    def display(self):
        """that prints in stdout
        the Rectangle instance with the character #
        """
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """defines the string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
