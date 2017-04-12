#!/usr/bin/python3
"""
Sends Post request via URL with request package
"""
import sys
import requests


if __name__ == "__main__":
    header = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=header)
    print(r.text)
