#!/usr/bin/python3
"""Holds Base class for the project"""
import os


class Base():
    """
    Base class

    Attributes
    ----------
    __nb_objects : int
        private class attribute, count the NUM of instances

    id : int
        public instance attribute, identificator for instance

    Methods:
    -------
    to_json_string : class method
        return a str for JSON serialization

    save_to_file : class method
        save serialization on a file
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def to_json_string(cls, list_dictionaries):
        """returns a JSON str representation of list_dictionaries """
        return str(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save serializations on a file"""
        # @list_objs have literal adresses of instances!! #
        if list_objs != None:
            dict_obj = [lists.to_dictionary() for lists in list_objs]
        else:
            list_objs = []

        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(dict_obj))
