#!/usr/bin/python3
def uniq_add(my_list):
    """
    Adds all unique integers in a list (only once for each integer).
    """

    x = 0
    values = set(my_list)
    for i in values:
        x += i

    return x
