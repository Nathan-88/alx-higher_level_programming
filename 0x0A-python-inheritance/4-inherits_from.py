#!/usr/bin/python3
"""check if the object is an instance of a class that inherited 
(directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """class inheritance"""
    return isinstance(obj, a_class) and not type(obj) == a_class
