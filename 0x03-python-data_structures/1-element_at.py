#!/bin/usr/python3
def element_at(my_list, idx):
    if my_list == []:
        return None
    elif idx >= len(my_list):
        return None
    elif idx < 0:
        return None
    return my_list[idx]
