#!/usr/bin/python3

"""This Define a class Square."""


class Square:
    """This represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("The size must be an integer")
        elif size < 0:
            raise ValueError("The size must be >= 0")
        self.__size = size
