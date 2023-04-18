#!/usr/bin/python3
""" This function computes the square of all
integers ina  matrix """


def square_matrix_simple(matrix=[]):
    new = amtrix.copy()
    for x in new:
        for y in range(len(x)):
            x[y] = x[y]**2
    return(new)
