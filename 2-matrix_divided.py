#!/usr/bin/python3
"""Module for matrix_divided method."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_msg)
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(err_msg)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_msg)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
