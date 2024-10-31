# Ohjelmisto 2 - Moduuli 11 - Tehtävä 2 - Ajellaan erilaisilla autoilla

import autot
import kilpailut

from random import randint
import os
import time

from colorama import Fore

# pääohjelma

# Kirjoita pääohjelma, jossa luot yhden sähköauton
# (ABC-15, 180 km/h, 52.5 kWh)
# ja yhden polttomoottoriauton
# (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus,
# käske autoja ajamaan kolmen tunnin verran
# ja tulosta autojen matkamittarilukemat.

if __name__ == '__main__':

    # luodaan autot

    kilpailijat = []

    kilpailijat.append(autot.Sähköauto("ABC-001", 240, 670))
    kilpailijat.append(autot.Sähköauto("ABC-002", 260, 870))
    kilpailijat.append(autot.Polttomoottoriauto("ABC-100", 160, 55))
    kilpailijat.append(autot.Polttomoottoriauto("ABC-200", 220, 75))

    # luodaan kilpailu

    kilpailu1 = kilpailut.Kilpailu("Ratapäivä", 700, kilpailijat)

    # Tyhjennetään ruutu uutta peliä varten
    os.system('cls')

    # Suoritetaan kilpailu

    kestoh = 0

    while kestoh < 3:

        # Ajetaan 1h kerralla
        for auto in kilpailijat:
            # Ajetaan jokaista autoa kerrallaan, auto muuttaa vauhtia ja liikkuu 1h
            kilpailu1.tunti_kuluu(auto, randint(-10,25))
        kestoh += 1

# Tulostetaan tulokset
print(f"{Fore.GREEN} == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === =={Fore.RESET}") # 80 chars
print(f"{Fore.GREEN}|        {Fore.RED}V A L M I S T A   T U L I !         T U L O K S E T:{Fore.GREEN}                   |{Fore.RESET}") # 81 chars
print(f"{Fore.GREEN} == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === =={Fore.RESET}") # 80 chars
kilpailu1.tulosta_tilanne()
print(f"{Fore.GREEN} == === ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== ===== === =={Fore.RESET}") # 80 chars
print("Paina ENTER poistuaksesi.")
# Odotetaan että käyttäjä painaa ENTER että jatketaan
input()

# Tyhjennetään ruutu ja tulostaan heippa ja odotetaan hetki
os.system('cls')
print("Heippa!")
time.sleep(3)

# Tyhjennetään ruutu ja peli on ohi
os.system('cls')
