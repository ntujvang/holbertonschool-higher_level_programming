#!/usr/bin/python3
def uniq_add(my_list=[]):
    num = []
    for i in my_list:
        if i not in num:
            num.append(i)
    return sum(num)
