#!/usr/bin/python3
"""Holds Base class for the project"""
import json
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
    to_json_string : Static method
        return a str for JSON serialization

    save_to_file : Class method
        save serialization on a file

    from_json_string : Static method
        return datatype from a JSON strin, deserialize

    create : Class method
        create and return a new instance from Square or Rectangle
        (cls.__name__)

    load_from_file : Class Methods
        return a list of new instances
        with attributes loaded from
        somewhere else
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        """returns a JSON str representation of list_dictionaries """
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """loads a json_string a return a list"""
        if json_string is not None or len(json_string) != 0:
            return json.loads(json_string)
        else:
            return []

    @classmethod
    def save_to_file(cls, list_objs):
        """save serializations on a file"""
        # @list_objs have literal adresses of instances!! #
        if list_objs is not None:
            dict_obj = [lists.to_dictionary() for lists in list_objs]
        else:
            list_objs = []

        with open(f"{cls.__name__}.json", 'w', encoding="utf-8") as a_file:
            a_file.write(cls.to_json_string(dict_obj))

    @classmethod
    def load_from_file(cls):
        """
        return a list of new instances
        with attributes loaded from somewhere else
        """
        if os.path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json", "r", encoding="utf-8") as a_file:
                a_list = []
                for dicts in cls.from_json_string(a_file.read()):
                    a_list.append(cls.create(**dicts))
            return a_list
        else:
            return []

    @classmethod
    def create(cls, **dictionary):
        """crate a new instance from Base"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
