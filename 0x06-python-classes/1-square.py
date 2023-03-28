#!/usr/bin/python3
""" This defines a class with a private instance attribute: size """


class Square:
    """ This defines the class Square """
    pass

    def __init__(self, size):
        """ Here the init method is defined to initialie the private
        instance attribute size

        Args:
            size: this is the size of the square defined
        """
        self.__size = size
