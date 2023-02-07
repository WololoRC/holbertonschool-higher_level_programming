#!/usr/bin/python3
"""Holds is_same_class function"""


def is_same_class(obj, a_class):
    """return True if @obj is instance of @a_class"""
    return issubclass(a_class, type(obj))
