#!/usr/bin/python3
"""Send request to URL
Display value of var X-Request-Id
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
