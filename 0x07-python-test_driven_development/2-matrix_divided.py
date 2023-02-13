#!/usr/bin/python3
"""
a function that divides all elements of a matrix.
All elements of the matrix should be divided by div,
rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """
    a function dives all elements in a matrix by div
    """
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(element, (int, float))
               for row in matrix for element in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    n = len(matrix[0])
    for row in matrix:
        if len(row) != n:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        rounded_row = []
        for element in row:
            rounded_element = round(element / div, 2)
            rounded_row.append(rounded_element)
        result.append(rounded_row)
    return result
