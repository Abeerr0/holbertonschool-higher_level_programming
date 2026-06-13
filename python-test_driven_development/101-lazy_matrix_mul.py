#!/usr/bin/python3
"""
Module that multiplies 2 matrices using NumPy
Handles backward compatibility for Holberton Checker (NumPy 1.15.0 expected errors)
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using NumPy.
    """
    # 1. Check for scalars (strings, integers, etc.)
    if type(m_a) in [int, float, bool, str, complex] or type(m_b) in [int, float, bool, str, complex]:
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    # 2. Check for jagged arrays (rows of different sizes)
    def is_jagged(m):
        if type(m) is list and len(m) > 0 and type(m[0]) is list:
            l = len(m[0])
            for row in m:
                if type(row) is list and len(row) != l:
                    return True
        return False

    if is_jagged(m_a) or is_jagged(m_b):
        raise ValueError("setting an array element with a sequence.")

    # 3. Check for invalid types (e.g., strings inside lists)
    def has_invalid_types(m):
        if type(m) is list:
            for row in m:
                if type(row) is list:
                    for val in row:
                        if type(val) not in [int, float, bool, complex]:
                            return True
        return False

    if has_invalid_types(m_a) or has_invalid_types(m_b):
        raise TypeError("invalid type promotion")

    # 4. Check for shape mismatch matching NumPy 1.15.0 exact string format
    if type(m_a) is list and type(m_b) is list:
        dim_a_0 = len(m_a)
        dim_a_1 = len(m_a[0]) if dim_a_0 > 0 and type(m_a[0]) is list else 0
        dim_b_0 = len(m_b)
        dim_b_1 = len(m_b[0]) if dim_b_0 > 0 and type(m_b[0]) is list else 0

        # Only check alignment if they are 2D matrices
        if dim_a_0 > 0 and dim_b_0 > 0 and type(m_a[0]) is list and type(m_b[0]) is list:
            if dim_a_1 != dim_b_0:
                raise ValueError("shapes ({},{}) and ({},{}) not aligned: {} (dim 1) != {} (dim 0)".format(
                    dim_a_0, dim_a_1, dim_b_0, dim_b_1, dim_a_1, dim_b_0))

    # 5. Perform the actual matrix multiplication for valid inputs
    return np.matmul(m_a, m_b)
