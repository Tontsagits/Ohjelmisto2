# Ohjelmisto 2 - Moduuli 10 - Tehtävä 2 - Talo ja sen hissit

class Hissi:
    def __init__(self, alin: int, ylin: int):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde: int):
        if kohde > self.ylin or kohde < self.alin:
            print(f"Ei sellaista kerrosta ({kohde}).")
            return
        print(f"Kerros: {self.kerros}")
        while kohde > self.kerros:
            self.kerros_ylös()
        while kohde < self.kerros:
            self.kerros_alas()
        return
    def kerros_ylös(self):
        self.kerros += 1
        print(f"Kerros: {self.kerros}")
        return
    def kerros_alas(self):
        self.kerros -= 1
        print(f"Kerros: {self.kerros}")
        return

class Talo:
    def __init__(self, alin: int, ylin: int, kpl: int):
        self.alin = alin
        self.ylin = ylin
        self.kpl = kpl
        self.hissit = [Hissi(self.alin, self.ylin) for _ in range(self.kpl)]
    def aja_hissiä(self, hissi: int, kohdekerros: int):
        self.hissit[hissi].siirry_kerrokseen(kohdekerros)

# Main

talo1 = Talo(1, 9, 3)
talo1.aja_hissiä(0, 5)
