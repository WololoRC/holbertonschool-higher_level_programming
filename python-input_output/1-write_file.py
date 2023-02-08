#!/usr/bin/python3
"""Holds: write_file Function"""


def write_file(filename="", text=""):
    """write on a file and return num og chars writen"""
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
