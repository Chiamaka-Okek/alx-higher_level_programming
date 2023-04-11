#!/usr/bin/python3
""" Defines a class with an exception """


class BaseGeometry:
    """ This class raises an exception if area not found """
    def area(self):
        """ define the module area without implementation """
        raise Exception("area() is not implemented")
