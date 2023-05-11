#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html_content = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html_content)))
    print("\t- content: {}".format(html_content))
    print("\t- utf8 content: {}".format(html_content.decode('utf-8')))
