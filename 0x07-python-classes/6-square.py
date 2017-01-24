#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """ this set of property and setter is for size
    """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ this set of property and setter is for determining
        the printing location of the square
    """
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            for i in range(len(value)):
                if value[i] < 0:
                    raise TypeError("position must be a tuple"
                                    + " of 2 positive integers")
                self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
    def area(self):
        return int(self.__size) * int(self.__size)

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for blank in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for n in range(self.__size + self.__position[0]):
                    if n < self.__position[0]:
                        print(" ", end="")
                    else:
                        print("#", end="")
                print("")
