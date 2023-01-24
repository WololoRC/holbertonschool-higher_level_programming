#!/usr/bin/python3
def print_sorted_dictionary(a_dictironary):
    """
    Prints a dictionary by ordered keys.
    """

    for i in sorted(a_dictironary):
        print("{}: {}".format(i, a_dictironary.get(i)))
