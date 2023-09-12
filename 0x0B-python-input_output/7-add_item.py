#!/usr/bin/python3
"""
load, add, save
"""
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

argv = len(sys.argv)
new_list = []
filename = "add_item.json"

if os.path.isfile(filename):
    new_list = load_from_json_file(filename)

for i in range(1, argv):
    new_list.append(str(sys.argv[i]))

with open(filename, 'a', encoding="utf-8") as f:
    save_to_json_file(new_list, filename)
