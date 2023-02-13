#!/usr/bin/python3
"""Holds: Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """
    A Rectangle that inherits from Base

    Attributes
    ----------

    """

    def __init__(self, width, height, x=0, y=0, id=None):

        args = [width, height, x, y]
        arg_names = ["width", "height", "x", "y"]
        for i, arg in enumerate(args):
            if type(arg) != int:
                raise TypeError(f"{arg_names[i]} must be an integer")
            else:
                pass

        args = [x, y]
        arg_names = ["x", "y"]
        for i, arg in enumerate(args):
            if arg < 0:
                raise ValueError(f"{arg_names[i]} must be >= 0")
            else:
                pass

        args = [width, height]
        arg_names = ["width", "height"]
        for i, arg in enumerate(args):
            if arg <= 0:
                raise ValueError(f"{arg_names[i]} must be > 0")
            else:
                pass

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """
    getters and setters from here
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be and integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int:
            self.__height = value
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value
        else:
            raise TypeError("width must be and integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is int:
            self.__x = value
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value
        else:
            raise TypeError("x must be and integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is int:
            self.__y = value
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value
        else:
            raise TypeError("y must be and integer")
    """
    end of getters/setters sections
    """
