#!/usr/bin/python3
"""Holds: save_to_json_file Function"""
import json


def save_to_json_file(my_obj, filename):
    """save @my_obj as a json file"""
    with open(filename, "w", encoding="utf-8") as my_file:
        json.dump(my_obj, my_file)
