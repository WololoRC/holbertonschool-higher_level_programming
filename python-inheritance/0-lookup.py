#!/usr/bin/python3
"""holds lookup function"""


def lookup(obj):
    """return a list of all avaliable atrributes
                    and methods.
    """
    return list(dir(obj))
