#!/usr/bin/python3
""" This defines a class with a two private instance attribute and
two public instances method
"""


class Square:
    """ This defines the class square """
    pass

    def __init__(self, size=0, position=(0, 0)):
        """ Here init is defined to initialize the private instances
        attribute size and position

        Args:
            size: size of the square.
            position: position of the square.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ Gets size of the square """
        return(self.__size)

    @property
    def position(self):
        """ Gets the position of the square """
        return(self.__position)

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

    @position.setter
    def position(self, value):
        """ Sets the position of the square and  raises requires exceptions"""
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positiove integers")

    def area(self):
        """ This returns the square area """
        a = self.__size * self.__size
        return(a)

    def my_print(self):
        """ This prints to stdout the square in character # at the required
        position. """
        if self.__size == 0:
            return('\n')
        else:
            [print("") for i in range(self.__position[1])]
            for i in range(self.__size):
                [print(" ", end="") for j in range(self.__position[0])]
                [print("#", end="") for k in range(self.__size)]
                print()
