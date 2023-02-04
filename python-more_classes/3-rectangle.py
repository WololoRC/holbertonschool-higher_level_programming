#!/usr/bin/python3
"""rectangue module: holds a class called Rectangle"""


class Rectangle:
    """A rectangle builder

    Attributes
    ---------
    __width : int (0 by default)
        width of a Rectangle instance
    __height : int (0 by default)
        height of a Rectangle instance
    """

    def __init__(self, width=0, height=0):
        if (type(width) != int):
            raise TypeError("width must be an integer")

        elif (type(height) != int):
            raise TypeError("height must be an integer")

        elif (width >= 0 and height >= 0):
            self.__height = height
            self.__width = width

        elif (width < 0):
            raise ValueError("width must be >= 0")

        elif (height < 0):
            raise ValueError("height must be >= 0")

    def __str__(self):
        """print a Rectangle instance"""
        if self.__height <= 0 or self.__width <= 0:
            return ""
        else:
            for i in range(self.__height - 1):
                print("#" * self.__width)
            print("#" * self.__width, end="")
        return ""

    def area(self):
        """return the area od a Rectangle instance"""
        return (self.__height * self.__width)

    def perimeter(self):
        """returns the perimeter of a Rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return 0

        return (2 * (self.__height + self.__width))

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width=0):
        """width setter

        Args
        ---------
        width : int (0 by default)
            Rectangle width

        Raises
        ------
        TypeError
            if type(width) != int
        ValueError
            if width < 0
        """

        if type(width) != int:
            raise TypeError("width must be an integer")

        elif width >= 0:
            self.__width = width

        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height setter"""
        return self.__height

    @height.setter
    def height(self, height=0):
        """height setter

        Args
        ---------
        height : int (0 by default)
            height width

        Raises
        ------
        TypeError
            if type(height) != int
        ValueError
            if height < 0
        """

        if type(height) != int:
            raise TypeError("height must be an integer")

        elif height >= 0:
            self.__height = height

        else:
            raise ValueError("height must be >= 0")
