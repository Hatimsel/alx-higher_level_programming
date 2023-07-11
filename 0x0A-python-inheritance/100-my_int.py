#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """a subclass of int"""
    def __eq__(self, value):
        """
        Invert == operator
        """
        return not (self is not value)

    def __ne__(self, value):
        """
        Invert != operator
        """
        return (self is not value)
