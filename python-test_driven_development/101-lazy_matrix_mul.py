#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
It contains one function: `lazy_matrix_mul(m_a, m_b)`.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using numpy.matmul.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        ndarray: The matrix product of m_a and m_b.
    """
    return np.matmul(m_a, m_b)
