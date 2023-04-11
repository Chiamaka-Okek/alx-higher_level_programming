#!/usr/bin/python3
""" This determines if an object is an instance of a class
that inherited directly or indirectly from a class """


def inherits_from(obj, a_class):
    """ This functions defines the instance of an objects inheritance """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return(True)
    else:
        return(False)
