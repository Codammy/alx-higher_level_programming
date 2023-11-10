#!/usr/bin/python3
"""defines a class Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """defines a Rectangle"""
    def __init__(self, width, height):
         BaseGeometry.integer_validator(self, "width", width)
         BaseGeometry.integer_validator(self, "height", height)
         self.__width = width
         self.__height = height

    def __str__(self):
        """returns string representaion of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height
