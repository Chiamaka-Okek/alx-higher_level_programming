#!/usr/bin/python3
""" Class Inheritance with area implementation """


class BaseGeometry:
    """ Define the super class """
    def area(self):
        """ Base area without implementation """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Checks the validity of the value parameter """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        a = self.__width * self.__height
        return(a)

    def __str__(self):
        return("[Rectangle]" + " " + str(self.__width) + "/" + str(self.__height))
