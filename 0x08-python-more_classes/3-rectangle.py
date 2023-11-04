#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creates an object"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        """should print the rectangle with the character #"""
        str = ""
        x, y = self.width, self.height
        if x == 0 or y == 0:
            return str
        for i in range(y):
            for j in range(x):
                str += Rectangle.print_symbol
            str += '\n' if i < (y-1) else ''
        return str

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        x, y = self.width, self.height
        return 2 * (x + y) if y != 0 and x != 0 else 0

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set width"""
        if width < 0:
            raise ValueError("width must be >= 0")
        if type(width) is not int:
            raise TypeError("width must be an integer")
        self.__width = width

    @property
    def height(self):
        """retrives height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set height"""
        if height < 0:
            raise ValueError("height must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        self.__height = height
