# Testing sibling object inheritance from multiple parent classes

class Kulkuneuvo:
    def __init__(self, nopeus: int):
        self.nopeus = nopeus


class Urheiluväline:
    def __init__(self, paino: int):
        self.paino = paino


class Polkupyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus: int, paino: float, vaihteet: int):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)

        self.vaihteet = vaihteet


pp = Polkupyörä(45, 18.7, 3)
print(pp.vaihteet)
print(pp.nopeus)
print(pp.paino)

