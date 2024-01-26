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
    with urllib.request.urlopen(f_url) as response:
        data = response.read()
        print(data.decode())
