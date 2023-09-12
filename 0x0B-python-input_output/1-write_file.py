#!/usr/bin/python3


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        chr_written = f.write(text)
    return chr_written
