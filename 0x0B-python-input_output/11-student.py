#!/usr/bin/python3
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
            for k, v in json.items():
                if hasattr(self, k):
                    setattr(self, k, v)
