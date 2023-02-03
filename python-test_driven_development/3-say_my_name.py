#!/bin/usr/python3
"""3-sat_mt_name: holds say_my_name func"""


def say_my_name(first_name, last_name=""):
    """
    print "My name is @first_name @last_name"

    Args
    ----
    first_name: str
        str to print.
    last_name: str
        str to print.

    Raises
    ------
    TypeError
        if first_name or last_name != str
    """
    if type(first_name) == str and type(last_name) == str:
        print(f"My name is {first_name} {last_name}")

    elif type(first_name) != str:
        raise TypeError("first_name must be a string")

    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
