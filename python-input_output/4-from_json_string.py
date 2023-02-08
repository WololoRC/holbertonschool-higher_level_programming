#!/usr/bin/python3
""'Holds: 4-from_json_string.py'""
import json


def from_json_string(my_str):
    """return from a json str a Python object"""
    return json.loads(my_str)
