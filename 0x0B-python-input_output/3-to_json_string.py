#!/usr/bin/python3
"""Define a function for JSON representation"""
import json


def to_json_string(my_obj):
    """Return JSON rep of an object(str)"""
    return json.dumps(my_obj)
