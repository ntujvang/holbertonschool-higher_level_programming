#!/usr/bin/python3
"""
Requesting for header info X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    header = 'X-Request-Id'
    with urllib.request.urlopen(url) as response:
        value = response.getheader(header)
    print(value)
