 #!/usr/bin/python3
class Square(object):
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """
def __init__(self, size=0):
        """initializes a square
        Args:
            __size (int): size of side of the square
        Return: None
        """
        self.__size = size
        if isinstance(self.__size, int) == False:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
