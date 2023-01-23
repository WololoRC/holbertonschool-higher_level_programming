#!/usr/bin/python3
def no_c(my_string):
    """
    removes all characters c and C from a string.
    """

    a_list = []
    a_str = ""

    for i in my_string:
        if (i != 'c') and (i != 'C'):
            a_str += i

    my_string = a_str

    return my_string
