# Ohjelmisto 2 - Moduuli 11 - Tehtävä 1 - Luokkahierarkia

class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi
    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")

class Lehti(Julkaisu):
    def __init__(self, nimi: str, ptoimittaja: str):
        super().__init__(nimi)
        self.ptoimittaja = ptoimittaja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Päätoimittaja: {self.ptoimittaja}")

class Kirja(Julkaisu):
    def __init__(self, nimi: str, tekija: str, sivuja: int):
        super().__init__(nimi)
        self.tekija = tekija
        self.sivuja = sivuja
    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Tekijä: {self.tekija}, {self.sivuja} sivua.")



aa = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aa.tulosta_tiedot()
kirja.tulosta_tiedot()
