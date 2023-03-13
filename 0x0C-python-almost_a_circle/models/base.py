#!/usr/bin/python3
"""Defines a base model class."""
import json


class Base:
    """Represent the base model.
    Represents the "base" for all other classes in project 0x0C*.
    Attributes:
        __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries is {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation
        of list_objs(i.e a list of instances who inherits from base)
        to a file
        to_dictionary converts to a dict and stores in a list
        """
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns list obj represented by json_str (json to python(list))"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set by creating a
        dummy instance as a placeholder for the actual instz attr and values
        """
        if cls.__name__ == "Rectangle":
            dummy_cls_obj = cls(5, 8)
        if cls.__name__ == "Square":
            dummy_cls_obj = cls(9)
        dummy_cls_obj.update(**dictionary)
        return dummy_cls_obj
