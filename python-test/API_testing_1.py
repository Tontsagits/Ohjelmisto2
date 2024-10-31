import requests

hakusana = input("Anna hakusana: ")

# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyyntö = "https://api.tvmaze.com/search/shows?q=" + hakusana

vastaus = requests.get(pyyntö).json()

# print(json.dumps(vastaus, indent=4))

# Käy läpi JSON rakennetta. Sisältää dictionary elementtejä sisäkkäin ja listoja
for entry in vastaus:
    print(f"{entry['show']['name']}: {entry['show']['type']}")
    print(f" - Rating: {entry['show']['rating']['average']}")
    print(f" - Schedule: {entry['show']['schedule']['days']}")
    # Tulostetaan JSON tiedosta aikataulu, jos sellainen on, muoto JSON on lista
    for day in entry['show']['schedule']['days']:
        print(f" - Schedule: {day}")