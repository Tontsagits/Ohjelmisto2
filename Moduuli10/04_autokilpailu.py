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
#os.system('cls')
# Tulostetaan lähtötilanne
#print("Lähtötilanne!")
#for auto in osallistujat:
#    print(f"{auto.rekisteritunnus}, {auto.huippunopeus} kmh, {auto.nopeus} kmh, {auto.kuljettumatka} km.")
# Odotetaan heti että pelaaja ehtii lukea tulokset
#time.sleep(5)


# Tyhjennetään ruutu uutta peliä varten
os.system('cls')
# Tulostetaan lähtötilanne
print("Osallistujat:")
kilpailu1.tulosta_tilanne()
# Odotetaan heti että pelaaja ehtii lukea tulokset
time.sleep(5)



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
        kilpailu1.tulosta_tilanne()
        # Odotetaan että pelaaja ehtii lukea tiedot
        time.sleep(1)

    if perilla:
        break

# Tyhjennetään ruutu lopullisten tulosten tulostamista varten
os.system('cls')
# Tulostetaan tulokset
print("Valmista tuli!")
kilpailu1.tulosta_tilanne()
# Odotetaan että pelaaja ehtii lukea tulokset
time.sleep(10)

# Tyhjennetään ruutu ja tulostaan heippa ja odotetaan hetki
os.system('cls')
print("Heippa!")
time.sleep(3)

# Tyhjennetään ruutu ja peli on ohi
os.system('cls')
