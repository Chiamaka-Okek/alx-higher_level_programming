#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    u = []
    for row in matrix:
        row_len = len(row)
        y = []
        for j in range(row_len):
            y.append(row[j]**2)
            u.append(y)
        return u
