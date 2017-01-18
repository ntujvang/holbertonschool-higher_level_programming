#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {i: my_dict[i] * 2 for i in my_dict}
    return new_dict
