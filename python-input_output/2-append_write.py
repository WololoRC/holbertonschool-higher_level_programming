#!/usr/bin/python3
"""Holds: append_write Function"""


def append_write(filename="", text=""):
    """Appends text and return NUM of chars"""
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
