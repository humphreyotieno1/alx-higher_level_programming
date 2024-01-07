#!/usr/bin/python3
"""SCcript that accepts a letter and send a POST request"""
import requests
import sys


if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    myLetter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {"q": myLetter}
    r = requests.post(url, data=data)

    try:
        body = r.json()
        if body == {}:
            print("No result")
        else:
            print("[{}] {}".format(body.get("id"), body.get("name")))
    except ValueError:
        print("Not a valid JSON")
