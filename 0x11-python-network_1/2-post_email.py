#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]  # Fixed: Values is not necessary.
    # Fixed: urlencode the email address as a parameter named 'email'
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    # Fixed: Use POST method for sending data
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
