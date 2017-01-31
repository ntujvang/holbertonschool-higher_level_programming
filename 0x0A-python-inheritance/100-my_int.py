#!/usr/bin/python3
class MyInt(int):
    def __ne__(self, value):
        return True

    def __eq__(self, value):
        return False
