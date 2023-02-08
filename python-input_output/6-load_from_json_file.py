#!/usr/bin/python3
"""Holds: load_from_json_file Function"""
import json


def load_from_json_file(filename):
    """load and return a json file as a python object"""
    with open(filename, "r", encoding="utf-8") as my_json:
        return json.load(my_json)
