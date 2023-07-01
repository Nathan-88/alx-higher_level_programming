#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""


import urllib.request
import sys
import urllib.parse
if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii') #data should be bytes
    req = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8')
    print(content)
