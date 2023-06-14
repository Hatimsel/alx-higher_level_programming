#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            new_row.append(element)
        new_matrix.append(new_row)

    rows = len(new_matrix)
    columns = len(new_matrix[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(columns):
            new_matrix[i][j] = new_matrix[i][j] ** 2
    print(new_matrix)
