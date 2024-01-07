#!/usr/bin/python3
"""Accepts a URL and send data to it
Displays value of the x-Request-Id
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as content:
        header = content.info()
        print(header.get("X-Request-Id"))
