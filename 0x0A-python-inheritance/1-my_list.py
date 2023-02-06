#!/usr/bin/python3
""" class of list and subclass of MyList"""


class MyList(list):
    """super class of list"""

    def __init__(self):
        """initializer for list"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
