#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """using list comprehension"""
    return [[sqr * sqr for sqr in sublist] for sublist in matrix]
