# Testing timer delay (sleep) and clear screen functions

from time import sleep

print("Lähtölaskenta alkaa:")

for i in range(10, 0, -1):
    sleep(3)
    print(f"{i}...")

print("VALMIS!")
