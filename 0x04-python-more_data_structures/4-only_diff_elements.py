#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = []
    for i in set_1:
        if i not in set_2:
            new_set.append(i)
    for n in set_2:
        if n not in set_1:
            new_set.append(n)
    return new_set
