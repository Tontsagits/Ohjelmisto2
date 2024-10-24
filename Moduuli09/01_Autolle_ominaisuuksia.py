# Ohjelmisto 2 - Moduuli 9 - Tehtävä 1 - Auto-olioille ominaisuuksia

class Auto:

    def __init__(self, rekisteritunnus: str, huippunopeus: int, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka
        print("Auto lisätty.")

turbosaabi = Auto("ABC-123", 142)

print(f"Auton tiedot\nRekisteritunnus: {turbosaabi.rekisteritunnus:s}\nHuippunopeus: {turbosaabi.huippunopeus}\nNopeus nyt: {turbosaabi.nopeus}\nKuljettu matka: {turbosaabi.kuljettumatka}")
