#!/usr/bin/python3

class MyList(list):
    """A list sub-class"""

    def print_sorted(self):
        """print a list sorted"""
        print(sorted(self))
