#!/usr/bin/python3
"""
Response header value
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        data = response.info()
        if ('X-Request-Id') in data:
            print(data['X-Request-Id'])
