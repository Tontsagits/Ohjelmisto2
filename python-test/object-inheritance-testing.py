# Testing sibling object inheritance from parent class

class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi: str, sukunimi: str):
        Työntekijä.työntekijöiden_lukumäärä += 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi

    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")
        return

class Tuntipalkkainen(Työntekijä):

    def __init__(self, etunimi, sukunimi, tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Tuntipalkka: {self.tuntipalkka}")
        return

class Kuukausipalkkainen(Työntekijä):

    def __init__(self, etunimi: str, sukunimi: str, kuukausipalkka: int):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f" Kuukausipalkka: {self.kuukausipalkka}")
        return

if __name__ == "__main__":

    työntekijät = []
    työntekijät.append(Tuntipalkkainen("Viivi", "Virta", 12.35))
    työntekijät.append(Kuukausipalkkainen("Ahmed", "Habib", 2750))
    työntekijät.append(Työntekijä("Pekka", "Puro"))
    työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))
    työntekijät.append(Tuntipalkkainen("Matti", "Meikäläinen", 15.90))
    työntekijät.append(Kuukausipalkkainen("Maija", "Mehiläinen", 3650))

    for t in työntekijät:
        t.tulosta_tiedot()
