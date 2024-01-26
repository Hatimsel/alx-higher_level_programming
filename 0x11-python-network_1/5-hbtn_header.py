#!/usr/bin/python3
"""
Response header value with requests
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(f"{r.headers['X-Request-Id']}")
