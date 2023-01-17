#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = list(set(set_1) ^ set(set_2))
    return(new)
