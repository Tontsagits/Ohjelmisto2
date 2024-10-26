# Ohjelmisto 2 - Moduuli 10 - Tehtävä 2 - Talo ja sen hissit

import hissi

class Talo:
    def __init__(self, alin: int, ylin: int, kpl: int):
        self.alin = alin
        self.ylin = ylin
        self.kpl = kpl
        self.hissit = [hissi.Hissi(self.alin, self.ylin) for _ in range(self.kpl)]
    def aja_hissiä(self, hissi: int, kohdekerros: int):
        print(f"Hissi {hissi} liikkuu...")
        self.hissit[hissi].siirry_kerrokseen(kohdekerros)

# Main

talo1 = Talo(1, 9, 3)
talo1.aja_hissiä(0, 5)
