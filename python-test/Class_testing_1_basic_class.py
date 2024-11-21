# Class testing 1 - creating basic class

class Helikopteri:
    helikopterien_lukumaara = 0

    def __init__(self, nopeus=0, korkeus=0, vari="Valkoinen", matkustajatmax=1, matkustajia=0, suunta=0):
        self.nopeus = nopeus
        self.korkeus = korkeus
        self.vari = vari
        self.matkustajatmax = matkustajatmax
        self.matkustajia = 0
        self.suunta = suunta
        Helikopteri.helikopterien_lukumaara += 1

    def korkeusmuutos(self, kmuutos: int):
        self.korkeus += kmuutos

    def suuntamuutos(self, smuutos: int):
        self.suunta += smuutos

    def nopeusmuutos(self, nmuutos: int):
        self.nopeus += nmuutos


heli1 = Helikopteri(0, 0, "Musta", 5, 0, 0)
heli1.korkeusmuutos(20)
heli1.suuntamuutos(45)
heli1.nopeusmuutos(30)

print(
    f"Väri: {heli1.vari}, Suunta: {heli1.suunta}, matkustajia: {heli1.matkustajia}, helikoptereita yhteensä: {Helikopteri.helikopterien_lukumaara}")
