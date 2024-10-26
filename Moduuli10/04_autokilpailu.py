# Ohjelmisto 2 - Moduuli 10 - Tehtävä 4 - Autokilpailu

import autot
import kilpailut

from random import randint

# Luodaan autot
osallistujat = []
for i in range(1,11):
    nopeus = randint(100,250)
    osallistujat.append(autot.Auto(f"ABC-{i}", nopeus))

# Luodaan kilpailu
kilpailu1 = kilpailut.Kilpailu('Suuri romuralli', 8000, osallistujat)

# Tulostetaan lähtötilanne
kilpailu1.tulosta_tilanne(osallistujat)

# Suoritetaan kilpailu
while True:
    kesto = 0
    for auto in osallistujat:
        # Ajetaan 1h kerralla, auto muuttaa vauhtia ja liikkuu
        kilpailu1.tunti_kuluu(auto, randint(-10,15))
        kesto += 1

        # Tarkastetaan onko joku jo maalissa, jos on lopetetaan
        if kilpailu1.kilpailu_ohi(auto):
            perilla = True
            break

        # Tulostetaan tilanne 10h välein
        if kesto % 10 == 0:
            kilpailu1.tulosta_tilanne(osallistujat)
    if perilla:
        break

# Tulostetaan tulokset
print("Valmista tuli!")
kilpailu1.tulosta_tilanne(osallistujat)
