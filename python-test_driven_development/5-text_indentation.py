#!/usr/bin/python3
"""5-text_indentation module: holds text_indetation func"""


def text_indentation(text):
    """
    indent a text with two "\n" after: ".",":","?"'s

    Properties
    ----------
    text : str
        A string to indent and print

    Raises
    ------
    TypeError
        if @text != string
    """

    x = 0

    if type(text) is str:
        if text.count(". ") > 0 and text.count(":   ") > 0:
            x = text.replace(". ", ".\n\n")
            x = x.replace("? ", "?\n\n")
            x = x.replace(": ", ":\n\n")
        else:
            x = text.replace(".", ".\n\n")
            x = x.replace("?", "?\n\n")
            x = x.replace(":", ":\n\n")
        print(x, end="")

    else:
        raise TypeError("text must be a string")
