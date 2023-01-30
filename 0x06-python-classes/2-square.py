 #!/usr/bin/python3
 """ defines a square """


class Square:
    """ square with private instance attribute size"""

def __init__(self, size=0):
        """
        Args:
            __size (int): size of side of the square
        Return: None
        """
        self.__size = size
        if isinstance(self.__size, int) == False:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
