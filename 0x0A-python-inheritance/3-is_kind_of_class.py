#!/usr/bin/python3
""" Checks if an object is an insctance of a class or
an inherited class """


def is_kind_of_class(obj, a_class):
    """ Defines a function that is an instance of a class or an
    inherited """
    if isinstance(obj, a_class):
        return(True)
    else:
        return(False)
