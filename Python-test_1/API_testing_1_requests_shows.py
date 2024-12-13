# API Testing 1 - creating requests from TV Show API

import requests

# import json

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

# vastaus = requests.get(pyynto)
vastaus = requests.get(pyynto).json()

# print(json.dumps(vastaus, indent=4))
# print(vastaus)

# Käy läpi JSON rakennetta. Sisältää dictionary elementtejä sisäkkäin ja listoja
for entry in vastaus:
    print(f"{entry['show']['name']}: {entry['show']['type']}")
    print(f" - Rating: {entry['show']['rating']['average']}")
    print(f" - Schedule: {entry['show']['schedule']['days']}")
    # Tulostetaan JSON tiedosta aikataulu, jos sellainen on, muoto JSON on lista
    for day in entry['show']['schedule']['days']:
        print(f" - Schedule: {day}")
