#!/usr/bin/python3
"""Defines a class square"""


class Square:
    """Defines a square by size
    Attributes:
        _size(int): Size of the square
    """
    def __init__(self, size=0):
        """ init method
        Args:
            size (int): Size of the square

        """

        self.__size = size
