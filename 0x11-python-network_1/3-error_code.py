#!/usr/bin/python3
"""
Error code
"""
import sys
import urllib.request
import urllib.error.HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            print(data.decode())
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
