# Ohjelmisto 2 - Moduuli 9 - Tehtävä 4 - Ajetaan kilpaa

from random import randint

class Auto:

    def __init__(self, rekisteritunnus: str, huippunopeus: int, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka
        print(f"Auto {self.rekisteritunnus} lisätty.")
        print(f"Auton tiedot\nRekisteritunnus: {self.rekisteritunnus:s}\nHuippunopeus: {self.huippunopeus}\nNopeus nyt: {self.nopeus}\nKuljettu matka: {self.kuljettumatka}")

    def kiihdytä(self, nopmuutos: int):
        if nopmuutos < 0:
            print(f"Auto {self.rekisteritunnus} muuttaa nopeuttaan {nopmuutos} km/h.")
        elif nopmuutos == 0:
            print(f"Auton {self.rekisteritunnus} nopeus ei muutu...")
        else:
            print(f"Auto {self.rekisteritunnus} lisää nopeuttaan {nopmuutos} km/h.")
        if 0 <= self.nopeus + nopmuutos <= self.huippunopeus:
            self.nopeus += nopmuutos
            print(f"Auton {self.rekisteritunnus} nopeus on nyt {self.nopeus} km/h.")
        elif self.nopeus + nopmuutos < 0:
            print(f"Auto {self.rekisteritunnus} pysähtyi ja on nyt paikallaan.")
            self.nopeus = 0
        elif self.nopeus + nopmuutos > self.huippunopeus:
            print(f"Auton {self.rekisteritunnus} huippunopeus {self.huippunopeus} km/h saavutettu.")
            self.nopeus = self.huippunopeus

    def kulje(self, aikatuntia: float):
        self.kuljettumatka += self.nopeus * aikatuntia
        print(f"Auto {self.rekisteritunnus} kulkee {self.nopeus} km/h nopeudella {aikatuntia:.2f} tuntia.\nYhteensä {self.nopeus * aikatuntia:.2f} kilometriä.")

autot = []
for i in range(1,11):
    autot.append(Auto(f"ABC-{i}", randint(100, 200)))

print(autot)
