#!/usr/bin/python3
"""
What's my status? with Requests
"""
import requests

if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print(
        'Body response:\n\t- type: {}\n\t- content: {}'.
        format(type(r.text), r.text))
