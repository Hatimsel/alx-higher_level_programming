#!/usr/bin/python3
"""
Error code with requests
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        if r.status_code == 200:
            print(f"{r.text}")
    except requests.exceptions.HTTPError:
        print("Error code: {}".format(r.status_code))
