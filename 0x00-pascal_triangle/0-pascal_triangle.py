#!/usr/bin/python3
"""
Interview question about the Pascal Triangle
Returns a list of integers repping the pascal triangle
"""


def pascal_triangle(n):
    """
    This function returns a list of lists of integers.
    representing pascal's triangle with n.
    """

    arr = [[] for i in range(n)]
    if n <= 0:
        return []

    for i in range(n):
        for j in range(i + 1):
            if j == 0 or j == i:
                arr[i].append(1)
            else:
                arr[i].append(arr[i - 1][j - 1] + arr[i - 1][j])
    return arr
