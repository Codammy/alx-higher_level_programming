#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """Rectangle that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """creates an object"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __del__(self):
        """deletes an object"""
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """should print the rectangle with the character #"""
        str = ""
        x, y = self.width, self.height
        if x == 0 || y == 0:
            return str
        for i in range(y):
            for i in range(x):
            str += Rectangle.print_symbol
        return str

    def __repr__(self):
        """return a string representation of the rectangle"""
        return ""

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        return 2 * (self.width + self.height) if self.width != 0 and self self.height != 0 else 0

    def __get_width(self):
        """retrieve width"""
        return self.width

    def __set_width(self, value):
        """set width"""
        self.__width = value

    def __get_height(self):
        """retrives height"""
        return self.height

    def __set_width(self, value):
        """set height"""
        return self.height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_2.area > rect_1.area else rect_1

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return Rectangle(size, size)

    width = property(self.__get_width, self.__set_width)
    height = property(self.__get_height, self.__set_height)
