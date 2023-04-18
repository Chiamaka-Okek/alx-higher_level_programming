#!/usr/bin/python3
""" This function returns a new dictionary with values multiplied
by 2 """


def print_sorted_dictionary(a_dictionary):
    """ Returns a new dictionary """
    for x, y in sorted(a_dictionary.items()):
        print("{}: {}".format(x, y))


def multiply_by_2(a_dictionary):
    for x, y in sorted(a_dictionary.items()):
        print("{}: {}".format(x, y))
