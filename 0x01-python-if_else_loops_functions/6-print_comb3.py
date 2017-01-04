#!/usr/bin/python3
for i in range(0, 9):
    for n in range(i + 1, 10):
        if (i != 8 or n != 9):
            print("{:d}{:d}".format(i, n), end=", ")
        else:
            print("{:d}{:d}".format(i, n))
