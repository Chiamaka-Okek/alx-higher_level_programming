#!/usr/bin/python3
""" Define a subclass Square that inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Define class Rectangle """
    def __init__(self, size):
        """ Initializes the class """
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """ Implement area """
        a = self.__size * self.__size
        return(a)

    def __str__(self):
        """ Defines the module str """
        return("[Rectangle]" + " " + str(self.__size) + "/" +
               str(self.__size))
