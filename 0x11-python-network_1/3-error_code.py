#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""


import urllib.request
import sys
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
    except URLError as e:
        print('Reason: ', e.reason)
