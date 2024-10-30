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
        print(f"| Rekisteritunnus | Auton huippunopeus | Auton nopeus nyt | Auton kulkema matka |")
        for auto in self.osallistujat:
            print(f"| {auto.rekisteritunnus:^15} | {auto.huippunopeus:18} | {auto.nopeus:16} | {auto.kuljettumatka:19} |")
        return

    def kilpailu_ohi(self, auto):
        if auto.kuljettumatka >= self.pituuskm:
            return True
        return False
