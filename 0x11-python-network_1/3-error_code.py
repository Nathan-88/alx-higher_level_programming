#!/usr/bin/python3
""" a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
