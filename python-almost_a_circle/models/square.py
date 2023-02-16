#!/usr/bin/python3
"""Holds: Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square

    Methods and Attributes
    inherits from Rectangle Class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Same logic as update Method from Rectangle"""
        if len(args) > 0:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[1]
                self.x = args[2]
                self.y = args[3]
            except Exception:
                pass
        else:
            try:
                self.id = kwargs.get('id', self.id)
                self.width = kwargs.get('size', self.width)
                self.height = kwargs.get('size', self.height)
                self.x = kwargs.get('x', self.x)
                self.y = kwargs.get('y', self.y)
            except Exception:
                pass

    """getter and setter"""
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        super().__init__(value, value)
    """end of getter/setter section"""
