#!/usr/bin/python3
"""a function that checks
if the object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """if the object is exactly an instance of the specified class"""
    return type(obj) is a_class
