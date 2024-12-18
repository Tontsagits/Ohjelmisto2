# Ohjelmisto 2 - Moduuli 12 - Tehtävä 2 - Säätiedot maailmalta

from colorama import Fore
import requests
import os
import time

# API
# Current weather data
# Call current weather data
# How to make an API call
# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
# Built-in geocoding
# Please use Geocoder API if you need automatic convert city names
# and zip-codes to geo coordinates and the other way around.
# Please note that API requests by city name, zip-codes and city id have been deprecated.
# Although they are still available for use, bug fixing and updates are no longer available
# for this functionality.
# Built-in API request by city name
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# Response format. JSON format is used by default.
# Units of measurement
# For temperature in Celsius use units=metric
# Multilingual support
# You can use the lang parameter to get the output in your language.
# We support the following languages that you can use with the corresponded lang values:
# lang=fi Finnish

os.system('cls' if os.name == 'nt' else 'clear')
api_url = "https://api.openweathermap.org/data/2.5/weather?"
api_key = "8891ed0ba67dbb011bea8d0213972a42"
api_lang = "fi"
api_units = "metric"
print()
city_name = str(input(
    f"   *** {Fore.LIGHTBLUE_EX}Anna {Fore.RED}kaupunki{Fore.LIGHTBLUE_EX}, jonka säätiedot haluat hakea: {Fore.RESET}"))
api_req = f"{api_url}q={city_name}&appid={api_key}&lang={api_lang}&units={api_units}"
api_resp = requests.get(api_req).json()
'''print()
for key, value in api_resp.items():
    print(key, value)
'''
print()
print(f"{Fore.LIGHTBLUE_EX} Kaupunki: {Fore.GREEN}{api_resp['name']}")
print(f"{Fore.LIGHTBLUE_EX}  Säätila: {Fore.GREEN}{api_resp['weather'][0]['description']}")
print(f"{Fore.LIGHTBLUE_EX}  Lämpötila: {Fore.GREEN}{api_resp['main']['temp']}{Fore.LIGHTBLUE_EX}'C")
print(f"{Fore.LIGHTBLUE_EX}  Vuorokauden")
print(f"{Fore.LIGHTBLUE_EX}  - Alin lämpötila: {Fore.GREEN}{api_resp['main']['temp_min']}{Fore.LIGHTBLUE_EX}'C")
print(f"{Fore.LIGHTBLUE_EX}  - Ylin lämpötila: {Fore.GREEN}{api_resp['main']['temp_max']}{Fore.LIGHTBLUE_EX}'C")
print(f"{Fore.LIGHTBLUE_EX}  Ilmanpaine: {Fore.GREEN}{api_resp['main']['pressure']} {Fore.LIGHTBLUE_EX}hPa")
print(f"{Fore.LIGHTBLUE_EX}  Ilmankosteusprosentti: {Fore.GREEN}{api_resp['main']['humidity']} {Fore.LIGHTBLUE_EX}%")
print(f"{Fore.LIGHTBLUE_EX}  Tuulen nopeus: {Fore.GREEN}{api_resp['wind']['speed']} {Fore.LIGHTBLUE_EX}m/s{Fore.RESET}")
print()
time.sleep(5)
