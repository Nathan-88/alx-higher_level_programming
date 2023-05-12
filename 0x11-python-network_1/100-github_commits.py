#!/usr/bin/python3
"""
a Python script that takes 2 arguments in order to solve this challenge
The first argument will be the repository name
The second argument will be the owner name
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don't need to check arguments passed to the script (number or type)
"""

import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    try:
        json = r.json()
        for i in range(10):
            print("{}: {}".format(json[i].get('sha'),
                                  json[i].get('commit').get('author').
                                  get('name')))
    except ValueError:
        pass
