#!/usr/bin/env python

import requests
import urllib.request
from bs4 import BeautifulSoup

def get_dinner():

    # Gather site
    url = "https://www.sio.no/mat-og-drikke/spisesteder-og-kaffebarer"
    response = requests.get(url);
    soup = BeautifulSoup(response.text, "html.parser")

    # Find OJD
    ojd = soup.find("span", string="Ole-Johan spiseri")
    ojd = ojd.parent.parent.parent.parent
    dagens = ojd.find("div", {"class":"dagensmiddag"})

    # Find and return todays dinner
    dinners = dagens.find_all("ul", {"class":"dinner"})
    middager = "    Dagens: " + " ".join(dinners[0].text.split(" ")[:-5]) + "\n"
    middager += "    Vegetar: " + " ".join(dinners[1].text.split(" ")[:-5])
    return middager


def main():
    print("Dagens middager på Ole-Johan spiseri er:")
    print(get_dinner())

if __name__ == "__main__":
    main()
