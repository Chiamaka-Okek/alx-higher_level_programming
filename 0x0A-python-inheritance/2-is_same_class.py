#!/usr/bin/python3
""" This determines the status of an object """


def is_same_class(obj, a_class):
    """ Defines a function to match exactly the class type """
    if type(obj) == a_class:
        return(True)
    else:
        return(False)
