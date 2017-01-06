#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    size = len(sys.argv) - 1
    for i in range(0, size):
        sum = sum + int(sys.argv[i + 1])
    print("{:d}".format(sum))
