#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display
the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
"""
import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    data = {"q": value}

    with requests.post(url, data=data) as r:
        try:
            json_data = r.json()
            if json_data:
                user_id = json_data['id']
                user_name = json_data['name']
                print("[{}] {}".format(user_id, user_name))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
