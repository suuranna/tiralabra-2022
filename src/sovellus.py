from tkinter import Tk, ttk, IntVar, StringVar
import json
import musicalbeeps
from aloitusNakyma import AloitusNakyma
from kappaleNakyma import KappaleNakyma
from opetusNakyma import OpetusNakyma

class KL:
    def __init__(self, juuri):
        self._juuri = juuri
        self._nakymaNyt = None
        self._muuttuja = None

    def aloita(self):
        self.nayta_etusivu()

        self._muuttuja = IntVar()
        self._muuttuja.set(0)

    def piilota_nakyma(self):
        if self._nakymaNyt:
            self._nakymaNyt.tuhoa()

        self._nakymaNyt = None

    def napin_painaminen(self):
        nuotit = [("C4", 0.1), ("C", 0.1), ("C", 0.1), ("E", 0.1), ("D", 0.1), ("D", 0.1), ("D",0.1), ("F", 0.1), ("E",0.1), ("E",0.1), ("D",0.1), ("D",0.1), ("C", 0.2)]
        for nuotti in nuotit:
            musicalbeeps.Player(volume = 1, mute_output = False).play_note(nuotti[0], nuotti[1])
        print("soitin ukko-nooan ;)")

    def lisaa_opetusdataa(self):
        arvo = self._muuttuja.get

    def siirry_kappalenakymaan(self):
        self.nayta_generoitu_kappale()

    def siirry_etusivulle(self):
        self.nayta_etusivu()

    def siirry_opetusdatan_lisaamiseen(self):
        self.nayta_opetusnakyma()

    def nayta_opetusnakyma(self):
        self.piilota_nakyma()
        self._nakymaNyt = OpetusNakyma(self._juuri, self.napin_painaminen, self.siirry_etusivulle)
        self._nakymaNyt.pakkaa()

    def nayta_generoitu_kappale(self):
        self.piilota_nakyma()
        self._nakymaNyt = KappaleNakyma(self._juuri, self.napin_painaminen, self.siirry_etusivulle)
        self._nakymaNyt.pakkaa()

    def nayta_etusivu(self):
        self.piilota_nakyma()

        self._nakymaNyt = AloitusNakyma(self._juuri, self.siirry_kappalenakymaan, self.siirry_opetusdatan_lisaamiseen)
        #self._nakymaNyt = AloitusNakyma(self._juuri, self.napin_painaminen)
        #self._nakymaNyt = AloitusNakyma(self._juuri, self.siirry_kappalenakymaan, tallennaJson)
        self._nakymaNyt.pakkaa()

def avaaJson():
    with open('data.json', 'r') as data:
        arvo = json.loads(data.read())["testi"]
        tallennettava.set(arvo)

def tallennaJson():
    with open('data.json', 'w') as data:
        arvo = json.dumps({"testi":tallennettava.get()})
        data.write(arvo)


ikkuna = Tk()
ikkuna.title("tiralabra")




tallennettava = IntVar()

avaaJson()

tallennettava.set(4)


tallennaJson()

kayttoliittyma = KL(ikkuna)
kayttoliittyma.aloita()

ikkuna.mainloop()
