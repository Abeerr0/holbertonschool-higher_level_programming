#!/usr/bin/python3
"""
Module that multiplies 2 matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices by using NumPy.
    """
    # معالجة النصوص والأرقام الفردية (Scalars)
    if type(m_a) in (int, float, bool, complex, str) or type(m_b) in (int, float, bool, complex, str):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        err_msg = str(e)
        # معالجة مشكلة عدم توافق الأبعاد (Shapes)
        if "mismatch" in err_msg or "aligned" in err_msg or "size" in err_msg or "shape" in err_msg:
            s_a = np.shape(m_a)
            s_b = np.shape(m_b)
            str_s_a = str(s_a).replace(" ", "")
            str_s_b = str(s_b).replace(" ", "")
            dim1 = s_a[1] if len(s_a) > 1 else s_a[0]
            dim0 = s_b[0]
            raise ValueError("shapes {} and {} not aligned: {} (dim 1) != {} (dim 0)".format(str_s_a, str_s_b, dim1, dim0))
        # أي خطأ ValueError آخر نرفعه زي ما هو
        raise e
    except TypeError:
        # معالجة وجود قيم غير رقمية داخل المصفوفة (مثل النصوص)
        raise TypeError("invalid data type for einsum")
