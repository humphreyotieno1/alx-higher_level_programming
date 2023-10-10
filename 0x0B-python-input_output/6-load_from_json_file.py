#!/usr/bin/python3
"""Define function that creates an obj"""
import json


def load_from_json_file(filename):
    """Create python object from JSON file"""
    with open(filename) as f:
        return json.load(f)
