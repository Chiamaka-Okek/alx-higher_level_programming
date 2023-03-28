#!/usr/bin/python3
""" This defines a class with private instance attribute and
public instance method """


class Square:
    pass

    def __init__(self, size=0):
        """ Here init is defined to initialize the private instance
        attribute size.

        Args:
            size: size of the square.
        """
        self.__size = size

    @property
    def size(self):
        """ Gets size of the square """
        return(self.__size)

    @size.setter
    def size(self, value):
        """ Sets size of the square and raises required exceptions """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ This returns the square area """
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        """ Prints to stdout the square in # character """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
