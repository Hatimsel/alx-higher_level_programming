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
        print(f"[{data['id']} {data['name']}]")
    except requests.exceptions.InvalidJSONError:
        print('Not a valid JSON')
    except requests.exceptions.JSONDecodeError:
        print('No result')
