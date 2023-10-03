#!/usr/bin/python3
"""Define matrix div function"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (list): list of lists of int or float
        div (int/float): divisor

    Raises:
        TypeError: if the matrix has non-numbers
        TypeError: if the matrix has rows of different sizes
        TypeError: if div is not an int or float
        ZeroDivisionError: if div is 0

    Returns:
        new matrix with dividends
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    message = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(message)

    new = []
    same_len = len(matrix[0])
    for lists in matrix:
        if type(lists) is not list:
            raise TypeError(message)
        if len(lists) != same_len:
            raise TypeError("Each row of the matrix must have the same size")
        new = []
        for i in lists:
            if not isinstance(i, (int, float)):
                raise TypeError(message)
            new.append(round(i/div, 2))
        new.append(new)
        return (new)
