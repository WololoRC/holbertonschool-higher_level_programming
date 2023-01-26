#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print value and return True if is Integer, else return False
    """

    try:
        print("{:d}".format(value))
        return True

    except TypeError:
        return False
