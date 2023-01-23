#!/usr/bin/python3
def max_integer(my_list):
    """
    Finds the biggest integer of a list.
    """

    my_list.sort()

    if (len(my_list) > 0):
        m = (len(my_list) - 1)
        return my_list[m]

    else:
        return None
