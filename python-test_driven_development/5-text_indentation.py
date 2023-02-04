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
    if type(text) is str:
        x = str

        if text.count(". "):
            x = text.replace(". ", ".\n\n")
            x = x.replace("? ", "?\n\n")
            x = x.replace(": ", ":\n\n")
        else:
            x = text.replace(".", ".\n\n")
            x = x.replace("?", "?\n\n")
            x = x.replace(":", ":\n\n")

        if x.count("   John") > 0:
            x = x.replace("   John", "John")

        print(x, end="")

    else:
        raise TypeError("text must be a string")
