#!/usr/bin/python3
""" This describes a class that inherits from list """


class MyList(list):
    """ This class inherits from list """
    def __init__(self):
        """ This initializes the class MyList using
        the super class list """

    def print_sorted(self):
        """ This module sorts a list in ascending order """
        print(sorted(self))
