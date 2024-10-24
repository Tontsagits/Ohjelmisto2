# Testing Object and Class with constructor

# luodaan luokka 'Koira'
# ja alustetaan konstruktorilla sinne vakio-ominaisuudet ilman oletusarvoja
class Koira():
    def __init__(self, nimi, syntymavuosi):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi

koira = Koira("Rekku", 2022)

print(f"{koira.nimi:s} on syntynyt vuonna {koira.syntymavuosi:d}")
