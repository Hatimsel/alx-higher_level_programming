#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and returns the
    number of characters written
    """
    count = 0
    with open(filename, "w", encoding='utf-8') as f:
        for i in text:
            f.write(i)
            count += 1
        return count
