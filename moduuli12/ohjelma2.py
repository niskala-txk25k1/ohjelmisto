#!/usr/bin/env python3
import requests
import sys


def main():
    location = (sys.argv[1] if len(sys.argv)==2 else input("Paikkakunta: "))

    f = open("api_key")
    api_key = f.read()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}".rstrip()
    print(url)
    res = requests.get(url).json()
    desc = (res["weather"][0]["description"])
    temp = (res["main"]["temp"]) - 273.15
    print (f"{temp:.2f} 'C, {desc}")

if __name__ == "__main__":
    main()
