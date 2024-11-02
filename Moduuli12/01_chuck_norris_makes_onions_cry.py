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

api_url = "https://api.chucknorris.io/jokes/random"

def on_key_press(event):
    global key_pressed
    key_pressed = True

keyboard.on_press(on_key_press)

key_pressed = False

while True:
    api_resp = requests.get(api_url).json()
    os.system('cls' if os.name == 'nt' else 'clear')
    # print(resp1)
    # print(json.dumps(resp1, indent=4))
    # print(f"Press and hold ESC to quit.")
    print()
    print(f"     Here are some random Chuck Norris FACTS!\n     Chuck Norris CAN press {Fore.RED}ANYKEY{Fore.RESET} to exit.\n     {Fore.GREEN}You just need to just any key to quit.{Fore.RESET}")
    print()
    print(f"{Fore.GREEN}*** {Fore.RED}{api_resp['value']} {Fore.GREEN}***{Fore.RESET}")
    time.sleep(7)
    # check for ESC key pressed down
#    if keyboard.is_pressed("esc"):
    # check if any key pressed
    if key_pressed:
        break

os.system('cls' if os.name == 'nt' else 'clear')
print()
print(f"          B y e !")
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')
