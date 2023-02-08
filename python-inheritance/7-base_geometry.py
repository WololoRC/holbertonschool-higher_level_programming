#!/usr/bin/python3
"""Holads BaseGeometry class"""


class BaseGeometry():
    """Documentation in progress"""

    def area(self):
        """Documentation in progress"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates integer"""

        if type(value) is int:
            if value > 0:
                return value
            else:
                raise ValueError(f"{name} must be greater than 0")
        else:
            raise TypeError(f"{name} must be an integer")
