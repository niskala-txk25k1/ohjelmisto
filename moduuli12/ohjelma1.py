#!/usr/bin/env python3
import requests
import json


def main():
    res = requests.get("https://api.chucknorris.io/jokes/random").json()
    print(res["value"])

if __name__ == "__main__":
    main()
