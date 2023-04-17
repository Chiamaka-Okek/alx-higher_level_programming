#!/usr/bin/python3
""" Thsi function add two numbers """


def add_integer(a, b=98):
    """ Returns the sum of two integers or two floats cast to an integer
    Args:
        a: first argument
        b: second argument
    Returns:
        The summation of two integers
    Raises:
        TypeError: if arguments are neither integers or floats
    """
    if type(a) == int and type(b) == int:
        return(a + b)
    elif type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
        return(a + b)
    elif type(a) != float and type(a) != int:
        raise Exception("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise Exception("b must be an integer")
