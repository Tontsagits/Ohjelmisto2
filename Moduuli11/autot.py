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
        return

    def kulje(self, aikatuntia: float):
        self.kuljettumatka += self.nopeus * aikatuntia
        return

class Sähköauto(Auto):

    def __init__(self, rekisteritunnus: str, huippunopeus: int, akkukapasiteetti: int):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukwh = akkukapasiteetti

class Polttomoottoriauto(Auto):

    def __init__(self, rekisteritunnus: str, huippunopeus: int, bensatankki: int):
        super().__init__(rekisteritunnus, huippunopeus)
        self.btankkilitraa = bensatankki
