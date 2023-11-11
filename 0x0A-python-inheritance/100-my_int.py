#!/usr/bin/python3
"""defines A class MyInt that inherits from int"""


class MyInt(int):
    """defines MyInt"""
    def __init__(self, value):
        """Init"""
        self.value = value

    def __eq__(self, value):
        """inverted equal"""
        return self.value != value

    def __ne__(self, value):
        """inverted not equal"""
        return self.value == value
