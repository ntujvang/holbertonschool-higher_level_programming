#!/usr/bin/python3
"""
Sending a request to display error codes via requests
"""
import sys
import requests


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except Exception as e:
        print("Error code: {}".format(r.status_code))
