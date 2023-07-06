#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests

with requests.get("https://alx-intranet.hbtn.io/status") as r:
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
