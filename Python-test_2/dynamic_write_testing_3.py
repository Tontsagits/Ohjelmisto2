# Dynamic write testing 3

import sys
import time

for i in range(100):
    sys.stdout.write(f"\rLoading... {i}%")
    sys.stdout.flush()
    time.sleep(0.1)
sys.stdout.write("\nDone!\n")
