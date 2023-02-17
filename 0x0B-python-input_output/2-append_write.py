#!/usr/bin/python3
"""a function that appends a string
at the end of a text file
"""


def append_write(filename="", text=""):
    """function definition
    """
    with open(filename, 'a', encoding="utf-8") as f:
        ap = f.write(text)
        return ap
