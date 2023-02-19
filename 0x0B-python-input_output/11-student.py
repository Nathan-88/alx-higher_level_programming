#!/usr/bin/python3
""" a simple implementation of a serialization
and deserialization mechanism
(concept of representation of an object to another format
without losing any information
and allow us to rebuild an object based on this representation)
"""


class Student():
    """defines a class of student
    """
    def __init__(self, first_name, last_name, age):
        """define instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ If attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__
        else:
            diction = {}
            if isinstance(attrs, list):
                if all(isinstance(attr, str) for attr in attrs):
                    for i in attrs:
                        if i in self.__dict__:
                            diction.update({i: self.__dict__[i]})
            return diction

    def reload_from_json(self, json):
        """ that replaces all attributes of the Student instance
        """
        if isinstance(json, dict):
            for k in self.__dict__.keys():
                if k in json:
                    self.__dict__.update({k: json[k]})
            return self.__dict__
