#!/usr/bin/python3
"""Script to get ID from Github API"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
