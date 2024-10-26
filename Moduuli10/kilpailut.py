from prettytable import PrettyTable

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
        results = PrettyTable(padding_width=5)
        results.field_names = ["Rekkari", "Huippunopeus", "Nopeus nyt", "Kuljettu matka"]
        rivi = []
        for osallistuja in self.osallistujat:
            rivi.append(osallistuja.rekisteritunnus)
            rivi.append(osallistuja.huippunopeus)
            rivi.append(osallistuja.nopeus)
            rivi.append(osallistuja.kuljettumatka)
            results.add_row(rivi)
        print(results)
        return

    def kilpailu_ohi(self, auto):
        if auto.kuljettumatka >= self.pituuskm:
            return True
        return False
