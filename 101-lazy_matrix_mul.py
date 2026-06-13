#!/usr/bin/python3
"""
Module to perform matrix multiplication using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy."""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not m_a or (isinstance(m_a, list) and not all(m_a)):
        raise ValueError("m_a can’t be empty")
    if not m_b or (isinstance(m_b, list) and not all(m_b)):
        raise ValueError("m_b can’t be empty")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("ma and mb can’t be multiplied")
