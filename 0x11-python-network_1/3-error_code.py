#!/usr/bin/python3
"""
request a body if error display statue code
"""
import urllib.request
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as url:
            s = url.read()
            print(s.decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
