#!/usr/bin/python3
"""defines a square class"""
class Square:
    """Square class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area"""
        return self.__size**2

    @property
    def get_size(self):
        return self.__size

    @size.setter
    def set_size(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
