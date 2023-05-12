#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is
needed)
The first argument will be your username
The second argument will be your password (in your case, a personal
access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don't need to check arguments passed to the script (number or type)
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get(url, auth=(username, password))
    try:
        json = r.json()
        print(json.get('id'))
    except ValueError:
        print("None")