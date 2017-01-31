#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        list1 = self[:]
        list1.sort(key=int)
        print(list1)
