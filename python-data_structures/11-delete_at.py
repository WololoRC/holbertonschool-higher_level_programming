#!/usr/bin/python3
def delete_at(My_list, idx):
    """
    Deletes the item at a specific position in a list.
    """

    if (idx < len(My_list)) and (idx > -1):
        del My_list[idx]
    else:
        pass

    return My_list
