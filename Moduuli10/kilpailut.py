from prettytable import PrettyTable

class Kilpailu:

    def __init__(self, nimi: str, pituuskm: int, osallistujat: list):
        self.nimi = nimi
        self.pituuskm = pituuskm
        self.osallistujat = osallistujat

    def tunti_kuluu(self, auto, nopmuutos, aika=1):
        auto.kiihdytä(nopmuutos)
        auto.kulje(aika)
        return

    def tulosta_tilanne(self, auto):
        result = PrettyTable(padding_width=5)
        result.field_names = ["Rekkari", "Huippunopeus", "Nopeus nyt", "Kuljettu matka"]
        result.sortby = "Kuljettu matka"
        rivi = []
        rivi.append(auto.rekisteritunnus)
        rivi.append(auto.huippunopeus)
        rivi.append(auto.nopeus)
        rivi.append(auto.kuljettumatka)
        result.add_row(rivi)
        print(result)
        return

    def kilpailu_ohi(self, auto):
        if auto.kuljettumatka >= self.pituuskm:
            return False
        return
