#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        str = "area() is not implemented"
        raise Exception(str)

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
