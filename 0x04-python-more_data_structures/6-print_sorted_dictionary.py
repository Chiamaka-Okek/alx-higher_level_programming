#!/usr/bin/python3
""" This function prints a dictionary by ordered keys """


def print_sorted_dictionary(a_dictionary):
    """ Prints keys """
    for x, y in sorted(a_dictionary.items()):
        print("{}: {}".format(x, y))
