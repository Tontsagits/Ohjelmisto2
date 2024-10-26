# Ohjelmisto 2 - Moduuli 9 - Tehtävä 4 - Ajetaan kilpaa

from random import randint, randrange
from time import sleep
import os
from prettytable import PrettyTable

class Auto:

    def __init__(self, rekisteritunnus: str, huippunopeus: int, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdytä(self, nopmuutos: int):
        if 0 <= self.nopeus + nopmuutos <= self.huippunopeus:
            self.nopeus += nopmuutos
        elif self.nopeus + nopmuutos < 0:
            self.nopeus = 0
        else:
            self.nopeus = self.huippunopeus

    def kulje(self, aikatuntia: float):
        self.kuljettumatka += self.nopeus * aikatuntia

os.system('cls')
print("Autokilpailu 1.0")
print("Tervetuloa!")
print("Kilpailu alkaa...")
sleep(2)
os.system('cls')
sleep(1)
autot = []
for i in range(1,11):
    autot.append(Auto(f"ABC-{i}", randint(100, 200)))

perilla = False

while True:
    for auto in autot:
        auto.kiihdytä(randrange(-10, 16))
        auto.kulje(1)
        if auto.kuljettumatka >= 10000:
            perilla = True
    if perilla:
        break

result = PrettyTable(padding_width=5)
result.field_names = ["Rekkari","Huippunopeus","Nopeus nyt","Kuljettu matka"]
result.sortby = "Kuljettu matka"
result.reversesort = True
for auto in autot:
    rivi = []
    rivi.append(auto.rekisteritunnus)
    rivi.append(auto.huippunopeus)
    rivi.append(auto.nopeus)
    rivi.append(auto.kuljettumatka)
    result.add_row(rivi)
print("Valmista tuli!")
print(result)
