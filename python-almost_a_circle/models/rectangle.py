#!/usr/bin/python3
"""Holds: Rectangle class"""


from models.base import Base


class Rectangle(Base):
    """
    A Rectangle that inherits from Base

    Attributes
    ----------
    height : int
        height of Rectangle

    width : int
        width of Rectangle

    Methods
    -------
    area : public
        returns area (width * height)

    display : public
        display a rectangle

    update : public
        update instance attributes

    to_dictionary : public
        return a dict representation of the instance

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

        self.x = x
        self.y = y
        super().__init__(id)
        self.height = height
        self.width = width

    def __str__(self):
        return (f"[Rectangle] ({self.id}) {self.x}"
                f"/{self.y} - {self.width}/{self.height}")

    def to_dictionary(self):
        """return a dict representations of instance"""
        key_names = ['x', 'y', 'id', 'height', 'width']
        new_dic = {}
        for i, j in enumerate(self.__dict__.values()):
            new_dic.update({key_names[i]: j})
        return new_dic

    def area(self):
        """area returns"""
        return self.__width * self.__height

    def display(self):
        """displat my rectangle"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """update instance attributes"""
        try:
            super().__init__(args[0])
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            pass

        try:
            self.id = kwargs.get('id', self.id)
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)
        except Exception:
            pass

    # getters/setters section #
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
    # end of getters/setters section #
