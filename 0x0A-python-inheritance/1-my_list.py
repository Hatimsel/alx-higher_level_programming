#!/usr/bin/python3
"""
Class MyList inherites from list
"""


class MyList(list):
    """
    class MyList
    """
    def print_sorted(self):
        """
        returns a sorted list
        """
        print(sorted(self))
