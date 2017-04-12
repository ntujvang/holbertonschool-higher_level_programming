#!/usr/bin/python3
"""
Using request to Post onto JSON via variable q
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    insert = {'q': value}
    r = requests.post('http://0.0.0.0:5000/search_user', data=insert)
    if r.json():
        print("[{}] {}".format(r.json()['id'], r.json()['name']))
    elif not r.json():
        print("No result")
    else:
        print("Not a valid JSON")
