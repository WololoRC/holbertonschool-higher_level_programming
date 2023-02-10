#!/usr/bin/python3
"""Holds: class_to_json Function"""


def class_to_json(obj):
    """
    return the dictionary description of an object for
    json serialization purposes
    """
    return obj.__dict__
