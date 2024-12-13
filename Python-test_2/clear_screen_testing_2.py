# Clear screen testing 2

# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')

clear()
print("Tervetuloa harjoittelemaan näytön tyhjentämistä Pythonilla.")
print("Tämä on testiteksti 1...")
# Sleep for 3 seconds before clearing the screen
tdelay = 3
print(f"Sleep for {tdelay} seconds then clear the screen...")
sleep(tdelay)
print("Clearing the screen...")
# Clearing the Screen
clear()
print("Screen cleared!")
print("Tämä on testiteksti 2...")
print("Heippa!")
