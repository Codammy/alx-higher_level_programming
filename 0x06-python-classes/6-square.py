#!/usr/bin/python3
"""defines an empty class"""
class Square:
    """Square"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiator"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """area of square"""
        return self.__size**2

    def my_print(self):
        """prints in stdout the square with character #"""
        if self.size == 0:
            print()
        p, q = self.position
        while q > 1:
            print()
            q -= 1
        for r in range(self.size):
            for i in range(p):
                print(" ", end="")
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

    @property
    def position(self):
        """gets pos"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of a square"""
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
