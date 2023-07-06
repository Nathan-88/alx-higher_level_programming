#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
You must use Basic Authentication with a personal access token as
password to access to your information (only read:user permission is
needed)
The first argument will be your username
The second argument will be your password (in your case, a personal
access token as password)
You must use the package requests and sys
"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    passwd = sys.argv[2]

    with requests.get(url, auth=(username, passwd)) as r:
        try:
            json_data = r.json()
            print(json_data.get('id'))
        except ValueError:
            print("None")
