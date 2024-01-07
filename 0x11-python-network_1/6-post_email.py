#!/usr/bin/python3
"""Script that sends POST request to Url
Email is the parameter"""
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    r = requests.post(url, data=data)
    content = r.json()
    print(content.get("email"))
