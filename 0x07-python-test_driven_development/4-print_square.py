#!/usr/bin/python3
"""contain print square function """


def print_square(size):
    """prints # * size in row and column"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
