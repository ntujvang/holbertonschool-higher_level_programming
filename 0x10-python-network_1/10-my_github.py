#!/usr/bin/python3
"""
Script to show my Github ID creds!
"""
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = "https://api.github.com/users"
    r = requests.get(url, auth=(user, pwd))
    print(r.json().get('id'))
