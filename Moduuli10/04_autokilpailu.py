# Ohjelmisto 2 - Moduuli 10 - Tehtävä 4 - Autokilpailu

import autot
import kilpailu

from random import randint, randrange
from prettytable import PrettyTable

osallistujat = []
for i in range(1,15):
    nopeus = randint(100,250)
    osallistujat.append(autot.Auto(f"ABC-{i}", nopeus))

kilpailu.Kilpailu('Suuri romuralli', 8000, osallistujat)



