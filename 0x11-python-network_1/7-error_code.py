#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and
displays the body of the response.
If the HTTP status code is greater than or equal to 400, print: Error
code: followed by the value of the HTTP status code
You must use the packages requests and sys
Usage: ./7-error_code.py <URL>
"""

import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
