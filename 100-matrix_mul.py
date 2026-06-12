#!/usr/bin/python3
"""Module for matrix_mul method."""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices."""
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
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for x in row:
            if type(x) not in (int, float):
                raise TypeError("m_b should contain only integers or floats")
    len_a = len(m_a[0])
    if not all(len(row) == len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    len_b = len(m_b[0])
    if not all(len(row) == len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    for r_a in m_a:
        row_res = []
        for c_b in range(len(m_b[0])):
            val = sum(r_a[i] * m_b[i][c_b] for i in range(len_a))
            row_res.append(val)
        res.append(row_res)
    return res
