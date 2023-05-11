#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""


import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get('X-Request-Id'))
