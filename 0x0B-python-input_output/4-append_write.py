#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, mode="a",encoding="UTF8") as file:
        return file.write(text)
