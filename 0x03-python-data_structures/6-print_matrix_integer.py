#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        row_len = len(row)
        for i in range(row_len):
            if x != row_len - 1: 
                print("{:d}".format(row[x]), end=' ')
            else:
                print("{:d}".format(row[x]), end='')
        print()
