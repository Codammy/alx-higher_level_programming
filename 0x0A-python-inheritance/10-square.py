#!/usr/bin/python3
"""defines a class Square based on Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a Square"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """returns string representaion of rectangle"""
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """area of rectangle"""
        return self.__size * self.__size
