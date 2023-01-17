#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    elif key not in a_dictionary.keys():
        a_dictionary.update({key: value})
    return a_dictionary
