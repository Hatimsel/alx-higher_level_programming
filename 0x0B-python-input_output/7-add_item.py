#!/usr/bin/python3
"""load, add, save"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if os.path.isfile("add_item.json"):
    lst = load_from_json_file('add_item.json')
else:
    lst = []
argv = sys.argv
for i in range(1, len(argv)):
    lst.append(argv[i])
save_to_json_file(lst, 'add_item.json')
