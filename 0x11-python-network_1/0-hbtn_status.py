#!/usr/bin/python3
"""
What's my status?
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    print(
        'Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'.
        format(type(data), data, data.decode()))
