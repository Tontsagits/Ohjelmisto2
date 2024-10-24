# Testing Object and Class with constructor and methods

# luodaan luokka 'Koira'
# ja alustetaan konstruktorilla sinne vakio-ominaisuudet ja yksi parametri oletusarvolla
class Koira():

    koiria_luotu  = 0

    def __init__(self, nimi, syntymavuosi, haukahdus="Vuh vuh"):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi
        self.haukahdus = haukahdus
        Koira.koiria_luotu += 1
        print(f"Luodaan koira: {nimi}")

    def hauku(self, kerrat):
        for _ in range(kerrat):
            print(f"{self.nimi} haukkuu: {self.haukahdus}")

# testausta ja tulosteita
koira1 = Koira("Rekku", 2022)
print(f"Koiria luotu: {Koira.koiria_luotu}")
koira2 = Koira("Musti", 2021, "Räyh räyh räyh")
print(f"Koiria luotu: {Koira.koiria_luotu}")
koira3 = Koira("Meteoriitti", 2019, "Viu viu")
print(f"Koiria luotu: {Koira.koiria_luotu}")

print(f"{koira1.nimi:s} on syntynyt vuonna {koira1.syntymavuosi:d}")
print(f"{koira2.nimi:s} on syntynyt vuonna {koira2.syntymavuosi:d}")
print(f"{koira3.nimi:s} on syntynyt vuonna {koira3.syntymavuosi:d}")

koira1.hauku(2)
koira2.hauku(5)
koira3.hauku(3)
