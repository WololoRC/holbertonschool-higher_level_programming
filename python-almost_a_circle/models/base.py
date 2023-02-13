#!/usr/bin/python3
"""Holds Base class for the project"""


class Base():
    """
    Base class

    Attributes
    ----------
    __nb_objects : int
        private class attribute, count the NUM of instances

    id : int
        public instance attribute, identificator for instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
