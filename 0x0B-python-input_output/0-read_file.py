#!/usr/bin/python3
"""a function that reads a text file (UTF8)
and prints it to stdout:
"""


def read_file(filename=""):
    """function definition
    """
    with open(filename, encoding="utf-8") as f:
        f_content = f.read()
        print(f_content)
