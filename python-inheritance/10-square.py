#!/usr/bin/python3
"""Holds Square class from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A Square []"""

    def __init__(self, size):
        self.__size = Rectangle.integer_validator(self, "size", size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """ size of a square :) """

        return self.__size ** 2
