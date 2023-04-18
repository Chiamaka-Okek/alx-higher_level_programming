#!/usr/bin/python3
""" This function updates a dictionary """


def print_sorted_dictionary(a_dictionary):
    """ Prints the keys in the dictionary """
    for x, y in sorted(a_dictionary.items()):
        print("{}: {}".format(x, y))


def update_dictionary(a_dictionary, key, value):
    """ Updates the dictionary """
    for x in a_dictionary:
        if x is key:
            a_dictionary[x] = value
        elif x is not key:
            a_dictionary[key] = value
        return(a_dictionary)
