# Ohjelmisto 2 - Moduuli 12 - Tehtävä 1 - Random Chuck Norris vitsi

import keyboard
import requests
# import json # for json.dumps method

import os
import time
from colorama import Fore

# chucknorris.io is a free JSON API for hand curated Chuck Norris facts.

# Retrieve a random chuck joke in JSON format.
# https://api.chucknorris.io/jokes/random
# Example response (dictionary):
'''{
"icon_url" : "https://api.chucknorris.io/img/avatar/chuck-norris.png",
"id" : "gFC7Fr6-R_CLzCYApLQ3TA",
"url" : "",
"value" : "if you shoot Chuck Norris, the bullet dies"
}'''

req1 = "https://api.chucknorris.io/jokes/random"

while True:
    resp1 = requests.get(req1).json()
    os.system('cls' if os.name == 'nt' else 'clear')
    # print(resp1)
    # print(json.dumps(resp1, indent=4))
    print(f"Press and hold ESC to quit.")
    print(f"{Fore.GREEN}*** {Fore.RED}{resp1['value']} {Fore.GREEN}***{Fore.RESET}\r")
    time.sleep(5)
    # check for ESC keypressed down
    if keyboard.is_pressed("esc"):
        break

os.system('cls' if os.name == 'nt' else 'clear')
print("Bye!")
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')
