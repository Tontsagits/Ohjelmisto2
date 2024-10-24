# Ohjelmisto 2 - Moduuli 9 - Tehtävä 2 - Auton vauhti muuttuu

class Auto:
    def __init__(self, rekisteritunnus: str, huippunopeus: int, nopeus=0, kuljettumatka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka
    def kiihdytä(self, nopmuutos: int):
        if nopmuutos < 0:
            print(f"Auto muuttaa nopeuttaan {nopmuutos} km/h.")
        elif nopmuutos == 0:
            print("Auton nopeus ei muutu...")
        else:
            print(f"Auto lisää nopeuttaan {nopmuutos} km/h.")
        if 0 <= self.nopeus + nopmuutos <= self.huippunopeus:
            self.nopeus += nopmuutos
            print(f"Auton nopeus on nyt {self.nopeus} km/h.")
        elif self.nopeus + nopmuutos < 0:
            print(f"Auto pysähtyi ja on nyt paikallaan.")
            self.nopeus = 0
        elif self.nopeus + nopmuutos > self.huippunopeus:
            print(f"Auton huippunopeus {self.huippunopeus} km/h saavutettu.")
            self.nopeus = self.huippunopeus

turbosaabi = Auto("ABC-123", 142)

print(f"Auton tiedot\nRekisteritunnus: {turbosaabi.rekisteritunnus:s}\nHuippunopeus: {turbosaabi.huippunopeus}\nNopeus nyt: {turbosaabi.nopeus}\nKuljettu matka: {turbosaabi.kuljettumatka}")

turbosaabi.kiihdytä(30)
turbosaabi.kiihdytä(70)
turbosaabi.kiihdytä(50)
print(f"Auton nopeus on nyt {turbosaabi.nopeus} km/h.")
turbosaabi.kiihdytä(-200)
print(f"Auton nopeus on nyt {turbosaabi.nopeus} km/h.")

