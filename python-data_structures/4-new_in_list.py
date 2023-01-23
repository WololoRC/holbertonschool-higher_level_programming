#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list
    at a specific position without modifying the original list
    """

    cp = my_list[:]

    if (idx >= len(my_list) or (idx < 0)):
        return my_list

    cp[idx] = element

    return cp
