#!/usr/bin/python3
"""
inverting equal operator with non-equal
"""


class MyInt(int):
    """
    class Myint inheriting from int
    """
    def __eq__(self, other):
        """
        inverts the equal operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        inverts the non-equal operator
        """
        return super().__eq__(other)
