# Ohjelmisto 2 - Moduuli 10 - Tehtävä 4 - Autokilpailu

import autot
import kilpailut

from random import randint
import os
import time

# Luodaan autot
osallistujat = []
for i in range(1,11):
    nopeus = randint(100,250)
    osallistujat.append(autot.Auto(f"ABC-{i}", nopeus))

# Luodaan kilpailu
kilpailu1 = kilpailut.Kilpailu('Suuri romuralli', 8000, osallistujat)

# Tyhjennetään ruutu uutta peliä varten
os.system('cls')
# Tulostetaan lähtötilanne
print(f" == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === ==") # 80 chars
print(f"|       A U T O K I L P A I L U            T E R V E T U L O A !                |") # 81 chars
print(f" == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === ==") # 80 chars

kilpailu1.tulosta_tilanne()
print("Paina ENTER niin aloitetaan kilpailu!")
# Odotetaan että käyttäjä painaa ENTER että jatketaan
input()



# Suoritetaan kilpailu
perilla = False
kesto = 0
while True:
    # Tyhjennetään ruutu pelin pelaamista varten
    os.system('cls')
    # Ajetaan 1h kerralla
    for auto in osallistujat:
        # Ajetaan jokaista autoa kerrallaan, auto muuttaa vauhtia ja liikkuu 1h
        kilpailu1.tunti_kuluu(auto, randint(-10,15))
        kesto += 1
        # Tarkastetaan saapuuko liikutettava auto perille, jos kyllä niin lopetetaan
        if kilpailu1.kilpailu_ohi(auto):
            perilla = True
            break

    # Tulostetaan tilanne 10h välein
    if kesto % 10 == 0:
        # Tulostetaan pelin tilanne välitieto
        print(f" == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === ==")  # 80 chars
        print(f"|          R A C E    I S     O N ! ! !                                         |") # 81 chars
        print(f" == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === ==")  # 80 chars
        kilpailu1.tulosta_tilanne()
        # Odotetaan hieman jotta numerot eivät vilise liian nopeasti
        time.sleep(0.5)

    if perilla:
        break

# Tyhjennetään ruutu lopullisten tulosten tulostamista varten
os.system('cls')
# Tulostetaan tulokset
print(f" == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === ==") # 80 chars
print(f"|            A U T O K I L P A I L U N              T U L O K S E T             |") # 81 chars
print(f" == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === ==") # 80 chars
kilpailu1.tulosta_tilanne()
print("Paina ENTER poistuaksesi.")
# Odotetaan että käyttäjä painaa ENTER että jatketaan
input()

# Tyhjennetään ruutu ja tulostaan heippa ja odotetaan hetki
os.system('cls')
print("Heippa!")
time.sleep(2)

# Tyhjennetään ruutu ja peli on ohi
os.system('cls')
