#!/usr/bin/python3

__name__ = "__main__"

"""
    print the number and list the arguments
"""
import sys

a_len = len(sys.argv) - 1
if a_len < 0:
    a_len = 0

print("{} arguments".format(a_len))

for cnt in range(1, a_len + 1):
    print("{}: {}".format(cnt, sys.argv[cnt]))
