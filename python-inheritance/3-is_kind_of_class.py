#!/usr/bin/python3
"""holds: is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    return true if @obj is a instance
    of a a_class of a sub class of it
    """
    return isinstance(obj, a_class)
