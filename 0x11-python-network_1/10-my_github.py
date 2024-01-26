#!/usr/bin/python3
"""
Search API
"""
import requests
import sys

if __name__ == "__main__":
    header = {'Accept': 'application/vnd.github+json'}
    data = {'username': [sys.argv[1], sys.argv[2]]}
    r = requests.get('https://api.github.com/user/',
                     params=data, headers=header)
    print(r.text)
