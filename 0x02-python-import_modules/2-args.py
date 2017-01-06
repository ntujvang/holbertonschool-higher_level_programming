#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = len(sys.argv) - 1
    if i == 0:
        print("{:d} argument.".format(i))
    elif i == 1:
        print("{:d} argument:".format(i))
    else:
        print("{:d} arguments:".format(i))
    if i >= 1:
        for n in range(0, i):
            print("{:d}: {}".format(n + 1, sys.argv[n + 1]))
