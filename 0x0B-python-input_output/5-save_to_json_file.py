#!/usr/bin/python3
"""Define function that writes object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write an obbject to a file using JSON rep"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
