#!/usr/bin/python3
"""
write_file function
"""


def write_file(filename="", text=""):
    """
    return the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chr_written = f.write(text)
    return chr_written
