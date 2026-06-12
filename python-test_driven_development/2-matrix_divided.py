#!/usr/bin/python3
"""Module for matrix_divided"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or not matrix:
        raise TypeError(err)
    
    for row in matrix:
        if type(row) is not list or not row:
            raise TypeError(err)
        for i in row:
            if type(i) not in (int, float):
                raise TypeError(err)
                
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
        
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
        
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    return [[round(i / div, 2) for i in row] for row in matrix]
