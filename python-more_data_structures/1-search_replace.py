#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    """

    new = my_list.copy()

    if (my_list.count(search) == 0):
        return new

    else:
        new[new.index(search)] = replace
        return search_replace(new, search, replace)
