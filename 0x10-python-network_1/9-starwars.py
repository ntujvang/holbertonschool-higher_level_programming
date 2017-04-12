#!/usr/bin/python3
"""
Using request to search through star wars API for various characters
"""
import sys
import requests


if __name__ == "__main__":
    name = []
    url = "https://swapi.co/api/people/?search=" + sys.argv[1]
    r = requests.get(url)
    results = r.json()["results"]
    i = r.json()["count"]
    for key in results:
        name.append(key["name"])
    print("Number of result: {:d}".format(i))
    for item in name:
        print(item)
