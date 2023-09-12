#!/usr/bin/python3


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as f:
        add_chrs = f.write(text)
    return add_chrs
