#!/usr/bin/python3
"""holds: inherits_from functions"""


def inherits_from(obj, a_class):
    """
    return True if @obj only inherits from a_class
    """
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
