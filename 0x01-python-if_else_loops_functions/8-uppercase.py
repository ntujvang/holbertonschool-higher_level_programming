#!/usr/bin/python3
def uppercase(str):
    i = len(str)
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            letter = chr(ord(i) - 32)
        else:
            letter = i
        print("{}".format(letter), end="")
    print("")
