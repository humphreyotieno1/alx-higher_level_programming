#!/usr/bin/python3
"""Define matrix multiplication function using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return multiplication of two matrices

    Args:
        m_a (list of lists of int/float): 1st matrix
        m_b (list of lists of int/float): 2nd matrix
    """

    return (np.matmul(m_a, m_b))
