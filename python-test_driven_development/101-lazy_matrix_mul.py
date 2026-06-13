#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It contains one function: `lazy_matrix_mul(m_a, m_b)`.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.matmul with strict validation

    matching NumPy 1.15.0 exact exception messages.
    """
    # 1. Check for scalar/string inputs
    if not isinstance(m_a, list) or any(not isinstance(r, list) for r in m_a):
        raise ValueError("Scalar operands are not allowed, use '*' instead")
    if not isinstance(m_b, list) or any(not isinstance(r, list) for r in m_b):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # 2. Check for rectangular matrix sizes (homogeneous rows)
    len_a = len(m_a[0]) if m_a else 0
    for row in m_a:
        if len(row) != len_a:
            raise ValueError("setting an array element with a sequence.")

    len_b = len(m_b[0]) if m_b else 0
    for row in m_b:
        if len(row) != len_b:
            raise ValueError("setting an array element with a sequence.")

    # 3. Check for element types (integers or floats)
    for row in m_a:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("Unsupported object type")

    for row in m_b:
        for val in row:
            if not isinstance(val, (int, float)):
                raise TypeError("Unsupported object type")

    # 4. Determine shapes for alignment validation
    if m_a == []:
        shape_a = (0,)
    elif m_a == [[]]:
        shape_a = (1, 0)
    else:
        shape_a = (len(m_a), len(m_a[0]))

    if m_b == []:
        shape_b = (0,)
    elif m_b == [[]]:
        shape_b = (1, 0)
    else:
        shape_b = (len(m_b), len(m_b[0]))

    # 5. Check for matrix multiplication shape alignment
    if len(shape_a) == 1 or len(shape_b) == 1:
        if m_a == []:
            raise ValueError(
                "shapes (0,) and {} not aligned: 0 (dim 0) != {} (dim 0)"
                .format(shape_b, shape_b[0])
            )
        if m_b == []:
            raise ValueError(
                "shapes {} and (0,) not aligned: {} (dim 1) != 0 (dim 0)"
                .format(shape_a, shape_a[1])
            )
    else:
        if shape_a[1] != shape_b[0]:
            raise ValueError(
                "shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)"
                .format(shape_a, shape_b, shape_a[1], shape_b[0])
            )

    return np.matmul(m_a, m_b)
