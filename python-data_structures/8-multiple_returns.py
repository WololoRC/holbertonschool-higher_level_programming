#!/usr/bin/python3
def multiple_returns(setence):
    """
    returns a tuple with the length of a string and its first character.
    """
    if (len(setence) > 0):
        new = len(setence), setence[:1]

    else:
        new = 0, None

    return new
