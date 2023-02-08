#!/usr/bin/python3
"""Holds: read_file Function"""


def read_file(filename=""):
    """Open an read line by line a file on the current directory"""

    with open(filename, 'r', encoding="utf-8") as a_file:
        for a_line in a_file:
            print(f"{a_line}", end="")
