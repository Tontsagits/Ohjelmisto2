# Ohjelmisto 2 - Moduuli 11 - Tehtävä 1 - Luokkahierarkia

class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi

class Lehti(Julkaisu):
    def __init__(self, nimi: str, ptoimittaja: str):
        super().__init__(nimi)
        self.ptoimittaja = ptoimittaja
    def tulosta_tiedot(self):
        print(f"{self.nimi}\nPäätoimittaja: {self.ptoimittaja}")
        return

class Kirja(Julkaisu):
    def __init__(self, nimi: str, tekija: str, sivuja: int):
        super().__init__(nimi)
        self.tekija = tekija
        self.sivuja = sivuja
    def tulosta_tiedot(self):
        print(f"{self.nimi}\nTekijä: {self.tekija}, {self.sivuja} sivua.")
        return

aa = Lehti("Aku Ankka", "Aki Hyyppä")
rs = Lehti("Roope Setä", "Hannu Hanhi")
mn = Lehti("Musta Naami", "Salama Vuf Vuf")
kirja1 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
kirja2 = Kirja("Sofian Maailma", "Jostein Gaarder", 608)

aa.tulosta_tiedot()
rs.tulosta_tiedot()
mn.tulosta_tiedot()
kirja1.tulosta_tiedot()
kirja2.tulosta_tiedot()
