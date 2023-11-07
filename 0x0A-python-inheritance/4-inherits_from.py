#!/usr/bin/python3


"""checks for instaance"""
def inherits_from(obj, a_class):
    """method"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
