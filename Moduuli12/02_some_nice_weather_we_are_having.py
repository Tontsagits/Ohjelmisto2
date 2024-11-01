# Ohjelmisto 2 - Moduuli 12 - Tehtävä 2 - Säätiedot maailmalta

from colorama import Fore

# API
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}

api_key = "8891ed0ba67dbb011bea8d0213972a42"
api_url = "https://api.openweathermap.org/data/2.5/weather"
place = str(input(f"{Fore.LIGHTBLUE_EX}Anna kaupunki jonka säätiedot haluat hakea: {Fore.RESET}"))

print(place)
