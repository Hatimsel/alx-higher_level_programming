#!/usr/bin/python3
"""
Response header value
"""
import sys
import urllib.request


url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    # print(response.info().['X-Request-Id'])
    # print(type(response.info()))
    data = response.info()
    if ('X-Request-Id') in data:
        print(data['X-Request-Id'])
