#!/usr/bin/python3
"""
Post an email
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    f_url = f"{url}?email={email}"
    req = urllib.request.Request(f_url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(data.decode())
