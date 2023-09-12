#!/usr/bin/python3
"""
read_file function
"""


def read_file(filename=""):
    """
    prints the content of a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print("{:s}".format(read_data))
