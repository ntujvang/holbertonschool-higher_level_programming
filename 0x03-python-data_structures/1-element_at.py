#!/bin/usr/python3
def element_at(mylist, idx):
    if idx >= len(mylist):
        return None
    if mylist == []:
        return None
    if idx < 0:
        return None
    else:
        return mylist[idx]
