#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return a key with the highest value on @a_dictionary
    """

    if a_dictionary:
        sort = sorted(a_dictionary, reverse=True)
        return sort[0]
