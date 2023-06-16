#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    new_matrix = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
    return new_matrix
