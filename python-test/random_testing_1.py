# Testing random module functions

from random import randint, randrange
from time import sleep

print(f"random randrage between 1 to 100: {randrange(1, 100)}")
print(f"random randit between 1 to 100: {randint(1, 100)}")

print(f"random randrage between -10 to 15: {randrange(-10, 15)}")
print(f"random randit between -10 to 15: {randint(-10, 15)}")

sleep(3)
