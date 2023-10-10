#!/usr/bin/python3
"""Define function to rep Pascal's triangle"""


def pascal_triangle(n):
    """Represent Pascal Triangle size n
    Returns:
        list of lists of integers to rep triangle
    """
    if n <= 0:
        return []

    tr = [[1]]
    while len(tr) != n:
        t = tr[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i +1])
        tmp.append(1)
        tr.append(tmp)
    return tr
