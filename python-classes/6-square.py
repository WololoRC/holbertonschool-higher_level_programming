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
    def __init__(self, size=0, position=(0, 0)):
        """
        Parameters
        ----------
        size : int, optional
            the size of the square (default 0)
        position : int, optional
            position to print square

        Raises
        ------
        TypeError:
            if size is not int.
            or position has not two positive numbers.
        ValueError:
            if size is < 0.
        """
        p = position

        if type(p) == tuple and len(p) == 2:
            for i in p:
                if type(i) == int and i >= 0:
                    continue
                else:
                    raise TypeError("position must be"
                                    " a tuple of 2 positive integers")

            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        if type(size) == int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Retrives @position"""

        return self.__position

    @position.setter
    def position(self, value):
        """Setts new position

        Parameters
        ----------
        value : int ,tuple
            Value for new position

        Raises:
            ValueError
                if value < 0
        """
        if type(position) == tuple and position[0] >= 0 and position[1] >= 0:
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    @property
    def size(self):
        """Retrives @size"""

        return self.__size

    @size.setter
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

        if type(value) == int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if self.__position[1] > 0:
            print("" * self.__position[1])
        if (self.__size != 0):
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(" " * self.__position[0] + "#" * self.__size)
                else:
                    print("#" * self.__size)
        else:
            print()
