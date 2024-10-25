# Testing Time module

import time

print("Lähtölaskenta alkaa:")

for i in range(10, 0, -1):
    time.sleep(3)
    print(f"{i}...")

print("VALMIS!")
