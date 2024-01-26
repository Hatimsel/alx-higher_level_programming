#!/usr/bin/python3
"""
Search API
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[2] if not None else ""
    r = requests.post(sys.argv[1], data={'q': q})
    try:
        data = r.json()
        print(f'[{data['id']} {data['name']}]')
    except requests.exceptions.InvalidJSONError:
        print('Not a valid JSON')
    except requests.exceptions.JSONDecodeError:
        print('No result')
