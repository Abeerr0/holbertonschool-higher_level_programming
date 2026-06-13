#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
It contains one function: `matrix_divided(matrix, div)`.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given number.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide the matrix by (integer or float).

    Returns:
        list: A new matrix with all elements divided by div,
        rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows of the matrix are not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is 0.
    """
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    msg_size = "Each row of the matrix must have the same size"

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(msg_type)

    for row in matrix:
        if type(row) is not list or len(row) == 0:
            raise TypeError(msg_type)
        for x in row:
            if type(x) not in (int, float):
                raise TypeError(msg_type)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(msg_size)

    return [[round(x / div, 2) for x in row] for row in matrix]
