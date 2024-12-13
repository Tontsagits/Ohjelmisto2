# Testing Object and Class

# luodaan luokka 'Koira'
class Koira():
    pass

# luodaa olio 'koira'
# koira on olio, joka kuuluu luokkaan Koira
# ja sillä on olio-kohtaisia ominaisuukia, jotka
# eivät siirry muille olioille
koira = Koira()
koira.nimi = "Rekku"
koira.syntymävuosi = 2022

print(f"{koira.nimi:s} on syntynyt vuonna {koira.syntymävuosi:d}")
