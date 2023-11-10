#!/usr/bin/python3
"""adds a new attribute to an object if its possible"""


def add_attribute(obj, name, desc):
    """adds a new attribute to an object if its possible"""
    try:
        obj.name = desc
    except:
        raise TypeError("can't add new attribute")
