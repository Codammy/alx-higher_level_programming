#!/usr/bin/python3
"""Technical interview preparation: Find a peak in an unsorted list"""


def find_peak(list_of_integers):
    """find a peak in a list(unsorted)"""
    b , a = list_of_integers[:2]
    for i in list_of_integers:
        if i > a and i > b:
            return i
        b = 
    return None
