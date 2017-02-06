#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF8") as file:
        linenum = 0
        for line in file:
            linenum += 1
        if (nb_lines <= 0) or (nb_lines >= linenum):
            nb_lines = linenum
        file.seek(0)
        while nb_lines > 0:
            print(file.readline(), end="")
            nb_lines -= 1
