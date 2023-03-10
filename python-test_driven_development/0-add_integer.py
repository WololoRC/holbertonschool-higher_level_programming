#!/usr/bin/python3
"""0-add_integer module, supplies add_integer function"""


def add_integer(a, b=98):
    """add two numbers.

    Args
    ----
    a : int or floar
    b : int or float

    Return
    ------
    a + b : int
    """

    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")

    elif ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
