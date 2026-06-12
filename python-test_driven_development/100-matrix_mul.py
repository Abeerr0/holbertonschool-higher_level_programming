#!/usr/bin/python3
"""Module for matrix_mul"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
        
    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")
        
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
        
    for row in m_a:
        for item in row:
            if type(item) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
                
    row_len_a = len(m_a[0])
    if not all(len(row) == row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_len_b = len(m_b[0])
    if not all(len(row) == row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
        
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            val = 0
            for k in range(len(m_b)):
                val += m_a[i][k] * m_b[k][j]
            row_result.append(val)
        result.append(row_result)
    return result
