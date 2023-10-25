#!/usr/bin/python3
"""defines an empty class"""
class Square:
    """Square"""
    def __init__(self, size=0):
        """instantiator"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area of square"""
        return self.__size**2

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """sets the size of a square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
