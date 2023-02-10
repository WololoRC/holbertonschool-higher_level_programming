#!/usr/bin/python3
"""Hols: student class"""


class Student():
    """
    A Student

    Atributes
    ---------
    first_name : str
        his name

    last_name : str
        his last name

    age : int
        his age

    Methods
    -------
    to_json:
        see below...
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return __dict__ for json pruposites"""

        if attrs is None:
            return self.__dict__

        else:
            return {k: v for k, v in self.__dict__.items() if k in attrs}

    def reload_from_json(self, json):
        """From a json file replace the attributes of a student"""
        if len(dic) > 0:
            self.first_name = json.get('name')
            self.last_name = json.get('last_name')
            self.age = json.get('age')
