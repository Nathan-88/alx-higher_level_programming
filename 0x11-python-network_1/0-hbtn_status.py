#!/usr/bin/python3
"""
Write a Python script that fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request
import chardet

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html_content = response.read()
    content_type = response.headers.get('content-type')
    charset = chardet.detect(html_content)['encoding']
    html_content = html_content.decode(charset)
    print("Body response:")
    print("\t- type: {}".format(type(html_content.encode('utf-8'))))
    print("\t- content: {}".format(html_content.encode('utf-8')))
    print("\t- utf8 content: {}".format(html_content.encode('utf-8').decode('utf-8')))
