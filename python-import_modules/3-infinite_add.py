#!/usr/bin/python3
__name__ = "__main__"
from sys import argv

"""
    Adds any amount of arguments
"""

x = 0

for i in range(1, len(argv)):
    x += int(argv[i])

print("{}".format(x))
