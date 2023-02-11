#!/usr/bin/python3
""" A function that adds attributes to an object"""
def add_attribute(obj, attr, value):
    """a function that adds a new attribute to an object if it’s possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

