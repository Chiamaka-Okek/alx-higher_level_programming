#!/usr/bin/python3
""" Defines a class inheritance """


class BaseGeometry:
    """ Define class BaseGeometry """
    def area(self):
        """ Defines an area without implementation """
        raise Exception("area() is not implementing")

    def integer_validator(self, name, value):
        """" This function validates the values passed """
        if issubclass(type(value), int) and type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> musst be greater than 0")


class Rectangle(BaseGeometry):
    """ Defines a class that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Inintialization of class Rectangle """
        super().__init__()
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
