#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= len(my_list) or idx < 0:
        return my_list
    new_list = []
    for i in range(0, len(my_list)):
        new_list.append(my_list[i])
    new_list[idx] = element
    return new_list
