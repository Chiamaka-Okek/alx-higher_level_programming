#!/usr/bin/python3
""" This describes a class that inherits from list """


class MyList(list):
    """ This class inherits from list """
    def __init__(self):
        """ Initializes the class based on the super class """
        super().__init__()

    def print_sorted(self):
        """ This module sorts a list in ascending order """
        print(sorted(self))
