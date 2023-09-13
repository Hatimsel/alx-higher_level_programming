#!/usr/bin/python3
"""
Search and Update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for line in content:
            f.write(line)
            if (search_string + " ") in line or (search_string + "\n") in line:
                f.write(new_string)
