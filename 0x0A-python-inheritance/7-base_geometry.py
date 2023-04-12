#!/usr/bin/python3
""" Defines a class that validates the parameter value """


class BaseGeometry:
    """ Defines class """
    def area(self):
        """ Defines module area without implementation """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Defines the module that validates parameter value """
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
