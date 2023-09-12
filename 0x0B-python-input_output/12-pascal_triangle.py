#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    return a list of lists of integers
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(1, n):
        row = [1]
        row.append(triangle[i - 1][j - 1] + triangle[i - 1][j] for j in range(1, i))
        row.append(1)
        triangle.append(row)

    return triangle
