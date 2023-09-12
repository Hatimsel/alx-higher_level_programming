#!/usr/bin/python3
"""
load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    creates an object from a json file
    """
    with open(filename, encoding="utf-8") as f:
        return (json.load(f))
