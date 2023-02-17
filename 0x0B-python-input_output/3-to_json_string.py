#!/usr/bin/python3
""" a function that returns the
JSON representation of an object (string):
"""


def to_json_string(my_obj):
    """defines the function
    """
    import json
    chigo = json.dumps(my_obj)
    return chigo
