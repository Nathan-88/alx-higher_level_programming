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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:
        **kwargs must be skipped if *args exists and is not empty
        """
        if kwargs and len(kwargs) > 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        else:
            self.id = args[0] if len(args) >= 1 else self.id
            self.width = args[1] if len(args) >= 2 else self.width
            self.height = args[2] if len(args) >= 3 else self.height
            self.x = args[3] if len(args) >= 4 else self.x
            self.__y = args[4] if len(args) >= 5 else self.y

    def to_dictionary(self):
        """returns dictionary representation of rectangle (it's attributes)"""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
