#!/usr/bin/python3
""" A function that multiples a matrix
"""


def matrix_mul(m_a, m_b):
    """defines m_a as matrix1 and
    m_b as matrix2
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(m_a[i], list) for i in range(len(m_a))):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(m_a[i], list) for i in range(len(m_a))):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(j, (int, float)) for i in m_a for j in i):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(j, (int, float)) for i in m_b for j in i):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    return [[sum(a*b for a, b in zip(X_row, Y_col))
            for Y_col in zip(*m_b)] for X_row in m_a]
