# Ohjelmisto 2 - Moduuli 10 - Tehtävä 4 - Autokilpailu

import autot
import kilpailut

from random import randint
#from prettytable import PrettyTable

# Luodaan autot
osallistujat = []
for i in range(1,11):
    nopeus = randint(100,250)
    osallistujat.append(autot.Auto(f"ABC-{i}", nopeus))

# Luodaan kilpailu
kilpailu1 = kilpailut.Kilpailu('Suuri romuralli', 8000, osallistujat)

# Suoritetaan kilpailu
while True:
    for auto in osallistujat:
        # Ajetaan 1h kerralla, auto muuttaa vauhtia ja liikkuu
        kilpailu1.tunti_kuluu(auto, randint(-10,15))
        # Tarkastetaan onko joku jo maalissa
        kilpailu1.kilpailu_ohi(auto)

        # Tulostetaan tilanne 10h välein
        kilpailu1.tulosta_tilanne(auto)
    if perilla:
        break
