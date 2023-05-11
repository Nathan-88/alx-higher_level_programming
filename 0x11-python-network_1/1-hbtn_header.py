#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
"""

if __name__ == "__main__":
    url = sys.argv[1]

    import urllib.request
    import sys
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
