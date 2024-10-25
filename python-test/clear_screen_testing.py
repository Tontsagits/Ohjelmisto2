# Clear screen testing

import os
from time import sleep

print("Tämä on testiteksti 1...")
# Sleep for 3 seconds before clearing the screen
print("Sleep for 3 seconds then clear the screen...")
sleep(3)
print("Clearing the screen...")
# Clearing the Screen
os.system('cls')
print("Screen cleared!")
print("Tämä on testiteksti 2...")
