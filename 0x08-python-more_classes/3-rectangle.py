#!/usr/bin/python3
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = int(width)
        self.__height = int(height)

    """ this set of prop/setter is for width
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = int(value)

    """ this set of prop/stter is for height
    """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = int(value)

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for n in range(self.__width):
                string += "#"
            string += "\n"
        string = string[:-1]
        return string
