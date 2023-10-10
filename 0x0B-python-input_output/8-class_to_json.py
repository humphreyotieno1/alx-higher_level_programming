#!/usr/bin/python3
"""Define function for JSON serialization"""


def class_to_json(obj):
    """Return dict rep for JSON serialization"""
    return obj.__dict__
