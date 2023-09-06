#!/usr/bin/python3
"""
matrix_divided function
divides all it's elements by div
returns a new matrix
"""


def matrix_divided(matrix, div):
    """
    Takes two positional arguments
    returns a new matrix the result
    of dividing matrix's elements by div
    """
    if not isinstance(matrix, list) or not \
            all(isinstance(row, list) and all(isinstance(val, (int, float)) for val in row) for row in matrix):
        raise TypeError('matrix must be a matrix \
(list of lists) of integers/floats')

    reference_length = len(matrix[0])
    if not all(len(row) == reference_length for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_mtx = []
    for row in matrix:
        divided_row = [round(val / div, 2) for val in row]
        new_mtx.append(divided_row)

    return new_mtx
