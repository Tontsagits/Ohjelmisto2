# Testing creating dynamic instances

class Hissi:
    def __init__(self, alin: int, ylin: int):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

class Talo:
    def __init__(self, alin: int, ylin: int, kpl: int):
        self.alin = alin
        self.ylin = ylin
        self.kpl = kpl
        #self.hissit = [Hissi(self.alin, self.ylin) for _ in range(self.kpl)]
        self.hissit = []
        for i in range(1,self.kpl+1):
            hissi_vname = f"hissi{i}"
            exec(f"self.{hissi_vname} = Hissi(self.alin, self.ylin)")
            #self.hissit.append(getattr(self, hissi_vname))
            self.hissit.append(hissi_vname)
        for hissi in self.hissit:
            print(hissi)
            print(getattr(self, hissi))

'''
it is just a question of where and how to store the association
between Hissi instances and their assigned variables?

Exactly. It's all about maintaining a clear association between
the dynamically named variables and the instances you create.
By storing these associations in a list, dictionary, or any other
data structure that allows easy access and manipulation,
you can ensure your code remains readable and maintainable.
The key is to have a reliable way to retrieve and utilize
these instances whenever needed.
'''

# Main
talo1 = Talo(1, 9, 3)
