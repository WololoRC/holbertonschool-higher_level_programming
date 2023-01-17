#!/usr/bin/python3
def uppercase(str):

    """ Prints a string in uppercase """
    for i in str:
        if 96 < ord(i):
            i = chr(ord(i) - 32)

        print("{}".format(i), end="")
    print()
