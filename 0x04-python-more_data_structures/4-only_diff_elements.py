#!/usr/bin/python3
""" Write a function that returns a set of a ll elements
present in only one set """


def only_diff_elements(set_1, set_2):
    x = set_1 ^ set_2
    return(x)
