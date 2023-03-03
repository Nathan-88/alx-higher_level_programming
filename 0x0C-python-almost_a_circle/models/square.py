#!/usr/bin/python3
"""the class Square that
inherits from Rectangle:
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square that inherits
    attributes from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """info about this method() is documented in the superclass
        update method()
        """
        self.id = args[0] if len(args) >= 1 else self.id
        self.size = args[1] if len(args) >= 2 else self.size
        self.x = args[2] if len(args) >= 3 else self.x
        self.y = args[3] if len(args) >= 4 else self.y

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of square (it's attributes)"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
