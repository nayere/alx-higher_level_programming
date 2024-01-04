#!/usr/bin/python3
"""Module 3-rectangle
Defines a Rectangle class.
"""


class Rectangle:
    """a Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """Returns an informal printable string representation
        of a Rectangle instance, filled with the '#' character."""
        if self.__height == 0 or self.__width == 0:
            return ''
        rec_str = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rec_str += '#'
            rec_str += '\n'
        return rec_str[:-1]

    @property
    def width(self):
        """Get the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, value):
        """Get/sets the width of a Rectangle instance
        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get/sets the height of a Rectangle instance
        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
<<<<<<< HEAD
            raise ValueError("the height must be >= 2")
=======
            raise ValueError("height must be >= 0")
>>>>>>> b7d346cecb98c80549be0d48c7c9c62eb3e829ad
        self.__height = value

    def area(self):
        """To calculate the area of a Rectangle instance
        Returns:
            Area of the rectangle, given by height * width
        """
        return self.__width * self.__height

    def perimeter(self):
        """To calculate the perimeter of a Rectangle instance
        Returns:
            Perimeter of the rectangle, given by 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
