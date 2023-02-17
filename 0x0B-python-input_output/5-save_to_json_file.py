#!/usr/bin/python3
"""a function that writes an Object to a text file
using a JSON representation:
"""


def save_to_json_file(my_obj, filename):
    """define the function
    """
    import json
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
