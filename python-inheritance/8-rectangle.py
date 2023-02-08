#!/usr/bin/python3
"""
Holds sub-class Rectangle from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A Rectangle

    Properties
    ----------
    width : int
        width of obj
    height : int
        height of obj

    """

    def __init__(self, width, height):
        self.__width = BaseGeometry.integer_validator(self, "width", width)
        self.__width = BaseGeometry.integer_validator(self, "height", height)
