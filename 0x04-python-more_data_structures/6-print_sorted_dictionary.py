#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for item in sorted(my_dict):
        print(item, my_dict[item], sep=": ")
