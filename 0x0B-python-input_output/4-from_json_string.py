#!/usr/bin/python3
"""Define function that does str-obj"""
import json


def from_json_string(my_str):
    """Return object rep by JSON str"""
    return json.loads(my_str)
