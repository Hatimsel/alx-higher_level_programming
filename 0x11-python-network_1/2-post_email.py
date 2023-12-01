#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as
a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    with urllib.request.urlopen(sys.argv[1], data) as response:
        s = response.read()
        print(s.decode("utf-8"))
