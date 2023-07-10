#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """MyList that inherits from list"""
    def print_sorted(self):
        """a function that sorts a list
        returns a sorted copy"""
        sorted_list = sorted(self)
        print(sorted_list)
