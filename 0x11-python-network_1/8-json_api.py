#!/usr/bin/python3
"""
Search API
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if not None else ""
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data={'q': q})
    try:
        data = r.json()
        if data == {}:
            print('No result')
        print(f"[{data.get('id')}] {data.get('name')}")
    except ValueError:
        print('Not a valid JSON')
