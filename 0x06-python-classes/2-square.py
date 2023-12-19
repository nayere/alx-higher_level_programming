#!/usr/bin/python3
""" We begin by defining a class Square."""


class Square:
    """ Representation of a square."""

    def __init__(self, size=0):
        """The Initialization of a new Square.
        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("the size required  must be an integer")
        elif size < 0:
            raise ValueError("also the size must be >= 0")
        self.__size = size
