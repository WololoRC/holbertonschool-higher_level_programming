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
        self.__height = BaseGeometry.integer_validator(self, "height", height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """return the area of a rectangle"""
        return self.__width * self.__height
