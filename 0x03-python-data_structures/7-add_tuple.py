#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_result = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return (my_result)
