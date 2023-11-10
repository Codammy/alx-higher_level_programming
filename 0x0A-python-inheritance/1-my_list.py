#!/usr/bin/python3
"""defines class MyList that inherits from list"""


class MyList(list):
    """Mylist"""
    def print_sorted(self):
        """prints the list, but sorted"""
        li = sorted(self)
        print(li)
