#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list of lists of integers
        or floats.
        div (int or float): The divisor used to divide each element of
        the matrix.

    Returns:
        list: A new matrix with all elements divided by the divisor,
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists) of
        integers/floats,
                   or if each row of the matrix doesn't have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is equal to zero.
    """
    r_count = 0
    c_count = 0

    for row in matrix:
        if c_count == 0:
            c_count = len(row)
        else:
            if len(row) != c_count:
                raise TypeError('Each row of the matrix must have the same size')

        for column in row:
            if type(column) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        r_count += 1

    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = [[0 for _ in range(c_count)] for _ in range(r_count)]

    for i in range(r_count):
        for j in range(c_count):
            new_matrix[i][j] = round(matrix[i][j] / div, 2)

    return new_matrix
