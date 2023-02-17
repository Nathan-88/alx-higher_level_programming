#!/usr/bin/python3
""" a function that creates an Object
from a “JSON file”:
"""


def load_from_json_file(filename):
    """defines the function
    """
    import json
    with open(filename) as f:
        return json.load(f)
