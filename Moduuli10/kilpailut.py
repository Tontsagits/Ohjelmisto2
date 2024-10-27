class Kilpailu:

    def __init__(self, nimi: str, pituuskm: int, osallistujat: list):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.osallistujat = osallistujat

    def tunti_kuluu(self, auto, nopmuutos: int, aika=1):
        auto.kiihdytä(nopmuutos)
        auto.kulje(aika)
        return

    def tulosta_tilanne(self):
        for auto in self.osallistujat:
            print(f"{auto.rekisteritunnus}, {auto.huippunopeus} kmh, {auto.nopeus} kmh, {auto.kuljettumatka} km.")
        return

    def kilpailu_ohi(self, auto):
        if auto.kuljettumatka >= self.pituuskm:
            return True
        return False
