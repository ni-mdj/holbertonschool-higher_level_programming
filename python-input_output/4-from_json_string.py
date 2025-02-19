#!/usr/bin/python3
'''
4-from_json_string.py
'''
import json
"""Module for from_json_string method."""


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)
