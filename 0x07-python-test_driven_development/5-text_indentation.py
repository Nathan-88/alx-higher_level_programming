#!/usr/bin/python3
"""a function that prints a text
with 2 new lines after each of these characters:
.,? and :
"""


def text_indentation(text):
    """
    splits a text into lines along "?", ":", "." followed by 2 new lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '?' or text[i] == '.' or text[i] == ':':
            print("{}".format(text[i]), end="")
            print("\n")
            continue
        if text[i - 1] == "?" or text[i - 1] == ":" or text[i - 1] == ".":
            continue
        print("{}".format(text[i]), end="")
