#!/usr/bin/python3
""" This is a subclass that inherits from class Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Define class Rectangle """
    def __init__(self, size):
        """ Initializes the class """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Implements area """
        a = self.__size * self.__size
        return(a)

    def __str__(self):
        """ Defines the module str """
        return("[Square]" + " " + str(self.__size) + "/" +
               str(self.__size))
