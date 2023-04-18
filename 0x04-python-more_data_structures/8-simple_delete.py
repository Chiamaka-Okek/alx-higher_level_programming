#!/usr/bin/python3
""" This function deletes a key in a dictionary """


def print_sorted_dictionary(a_dictioanry):
    """ Prints the keys in the dictionary """
    for x, y in sorted(a_dictionary.items()):
        print("{}: {}".format(x, y))


def simple_delete(a_dictionary, key=""):
    """ Deletes a key """
    if key in list(a_dictionary):
        del a_dictionary[key]
    return(a_dictionary)
