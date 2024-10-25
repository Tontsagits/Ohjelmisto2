# Dynamic write testing 2

import time

for i in range(100):
    print(f"\rLoading... {i}%", end="")
    time.sleep(0.1)
print("\nDone!")
