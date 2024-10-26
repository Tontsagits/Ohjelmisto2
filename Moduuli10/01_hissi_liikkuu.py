# Ohjelmisto 2 - Moduuli 10 - Tehtävä 1 - Hissi liikkuu ylös ja alas

class Hissi:
    def __init__(self, alin: int, ylin: int):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def siirry_kerrokseen(self, kohde):
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

# Main

hiss1 = Hissi(1, 9)
hiss1.siirry_kerrokseen(9)
hiss1.siirry_kerrokseen(34)
