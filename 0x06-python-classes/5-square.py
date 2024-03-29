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

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.size == 0:
            print()
        for r in range(self.size):
            for c in range(self.size):
                print("#", end="")
            print()

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
