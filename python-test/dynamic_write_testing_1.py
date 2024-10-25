# Dynamic write testing 1

import sys
import time

def countdown_timer(seconds):
    for remaining in range(seconds, 0, -1):
        sys.stdout.write("\rTime left: {:2d} seconds".format(remaining))
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rTime's up!            \n")

# Example usage
countdown_timer(10)
