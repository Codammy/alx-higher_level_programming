#!/usr/bin/python3
"""adds a new attribute to an object if its possible"""


def add_attribute(obj, name, desc):
    """adds a new attribute to an object if its possible"""
    try:
        setattr(obj, name, desc)
    finally:
        if name not in dir(obj):
            raise TypeError("can't add new attribute")
