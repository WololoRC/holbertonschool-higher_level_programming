#!/usr/bin/python3
"""4-prinst_square module: holds print_square function"""


def print_square(size):
    """
    print a sqaure of sieze @size.

    Parameters
    ----------
    size : int
        size of square

    Raises
    ------
    ValueError
        if @size < 0

    TypeError
        if @size != int
    """

    if type(size) is int and size >= 0:
        for i in range(size):
            print("#" * size)

    elif type(size) is int and size < 0:
        raise ValueError("size must be >= 0")

    else:
        raise TypeError("size must be an integer")
