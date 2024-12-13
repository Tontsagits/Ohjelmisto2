# Clear screen testing 3

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

tdelay = 9
clear()
print(f"-== === ===== ===== ===== ===== ===== ===== ===== ===== === ==-")
print(".")
print(". Tervetuloa harjoittelemaan näytön tyhjentämistä Pythonilla.")
print(".")
print(".")
print(".          Tämä on IKKUNA 1")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(f". Clearing the screen in {tdelay} s...")
print(f"-== === ===== ===== ===== ===== ===== ===== ===== ===== === ==-")
# Sleep for 3 seconds before clearing the screen
sleep(tdelay)
# Clearing the Screen
clear()
print(f"-== === ===== ===== ===== ===== ===== ===== ===== ===== === ==-")
print(".")
print(". Tervetuloa harjoittelemaan näytön tyhjentämistä Pythonilla.")
print(".")
print(".")
print(".          Tämä on IKKUNA 2")
print(".")
print(".")
print(".")
print(".")
print(".")
print(".")
print(f". Clearing the screen in {tdelay} s...")
print(f"-== === ===== ===== ===== ===== ===== ===== ===== ===== === ==-")
sleep(tdelay)
# Clearing the Screen
clear()
print()
print()
print("                   Bye!")
print()
