#!/usr/bin/python3
""" This defines a class with a private instance attribute that also handles
exceptions
"""


class Square:
    """ This defines the class Square """
    pass

    def __init__(self, size=0):
        """ Here the init is defined to initialize the private instance
        attribute size.In addition, exceptions are raised to handle the
        datatype of the field size and also it's value.

        Args:
            size: size of the square.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ This returns the square area """
        a = self.__size * self.__size
        return(a)
