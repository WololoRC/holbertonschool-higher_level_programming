#!/usr/bin/python3
"""
Defines a class called Square

"""


class Square:
    """
    A Square

    Attributes
    ---------
    size : int
        the size of the square

    """
    __size = 0
    def __init__(self, size=0):
        """
        Parameters
        ----------
        size : int, optional
            the size of the square (default 0)

        Raises
        ------
        TypeError
            if size is not int
        ValueError.
            if size is < 0
        """

        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")


    @Square.self.__size.setter
    def size(self, value):
        """Setts new size

        Parameters
        ----------
        size : int, optional
            the size of the square (default 0)

        Raises
        ------
        TypeError
            if size is not int
        ValueError.
            if size is < 0
        """

        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """Retrives @size"""

        return self.__size


    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
