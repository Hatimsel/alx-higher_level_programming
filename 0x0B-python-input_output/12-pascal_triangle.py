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

    for i in range(n):
        row = [1]
        if triangle:
            prev_row = triangle[-1]
            row.extend(prev_row[j - 1] + prev_row[j] for j in range(1, i))
            row.append(1)
            triangle.append(row)

    return triangle
