#!/usr/bin/python3
<<<<<<< HEAD
"""defines a square class"""
class Square:
    """Square class"""
    def __init__(self, size=0):
=======
"""defines an empty class"""


class Square:
    """Square"""
    def __init__(self, size=0):
        """instantiator"""
>>>>>>> 26b329fe4d7bf44546285de09deb4e630d05b1df
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
<<<<<<< HEAD
        """Area"""
        return self.__size**2

    @property
    def get_size(self):
        return self.__size

    @size.setter
    def set_size(self, size=0):
=======
        """area of square"""
        return self.__size**2

    @property
    def size(self):
        """gets size"""
        return self.__size

    @size.setter
    def size(self, size=0):
        """sets the size of a square"""
>>>>>>> 26b329fe4d7bf44546285de09deb4e630d05b1df
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
