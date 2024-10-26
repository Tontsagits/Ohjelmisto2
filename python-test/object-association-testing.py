# Testing object association between object and classes

from random import randint

# luodaan luokka Koira

class Koira:
    def __init__(self, nimi, syntymävuosi, haukahdus="Vuh-vuh"):
        self.nimi = nimi
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus

    def hauku(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " haukkuu: " + self.haukahdus)
        return

class Hoitola:
    def __init__(self):
        self.koirat = []

    def koira_hoitoon(self, koira):
        self.koirat.append(koira)
        print(f"Koira {koira.nimi} kirjattu hoitoon.")
        return

    def koira_ulos(self, koira):
        self.koirat.remove(koira)
        print(f"Koira {koira.nimi} kirjattu ulos hoidosta.")
        return

    def tervehdi_koiria(self, kerrat):
        for koira in self.koirat:
            koira.hauku(kerrat)

    def koirat_haukkuu(self):
        for koira in self.koirat:
            koira.hauku(randint(1, 5))

# Pääohjelma

koira1 = Koira("Murre", 2020, "Räyh räyh")
koira2 = Koira("Musti", 2021, "Möyk möyk")
koira3 = Koira("Meteoriitti", 2022, "Viu viu")
koira4 = Koira("Vuffe", 2023)
koira5 = Koira("Rekku", 2024, "Möh möh")

hoitola1 = Hoitola()

hoitola1.koira_hoitoon(koira1)
hoitola1.koira_hoitoon(koira2)
hoitola1.tervehdi_koiria(1)
hoitola1.koirat_haukkuu()

hoitola1.koira_hoitoon(koira3)
hoitola1.koira_hoitoon(koira4)
hoitola1.koira_hoitoon(koira5)
hoitola1.koirat_haukkuu()
