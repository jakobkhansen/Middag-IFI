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
    ojd = ojd.find("div", {"class":"dagensmiddag"})

    # Find and return todays dinner
    dinners = ojd.find_all("ul", {"class":"dinner"})

    for i in range(len(dinners)):
        dinners[i] = dinners[i].text.replace("Allergener: se merking på buffeten.", "")



    middager = "  Dagens: " + dinners[0] + "\n"
    middager += "  Vegetar: " + dinners[1]
    return middager


def main():
    print("Dagens middager på Ole-Johan spiseri er:")
    print(get_dinner())

if __name__ == "__main__":
    main()
