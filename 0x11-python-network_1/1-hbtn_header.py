#!/usr/bin/python3
"""
Fetch X-Request-Id from header response with url
introduced as argument
"""
import urllib.request
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
