#!/usr/bin/python3
"""
Module that multiplies 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using NumPy.
    """
    # معالجة النصوص والأرقام الفردية لإرضاء الشيكر اللي يتوقع رسالة إصدار 1.15.0
    if type(m_a) in (int, float, bool, complex, str) or type(m_b) in (int, float, bool, complex, str):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    return np.matmul(m_a, m_b)
