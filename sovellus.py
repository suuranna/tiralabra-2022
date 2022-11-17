from tkinter import Tk, ttk
import musicalbeeps
from aloitusNakyma import AloitusNakyma
from kappaleNakyma import KappaleNakyma
from opetusNakyma import OpetusNakyma

class KL:
    def __init__(self, juuri):
        self._juuri = juuri
        self._nakymaNyt = None

    def aloita(self):
        self.nayta_etusivu()

    def piilota_nakyma(self):
        if self._nakymaNyt:
            self._nakymaNyt.tuhoa()

        self._nakymaNyt = None

    def napin_painaminen(self):
        nuotit = [("C", 1), ("C", 1), ("C", 1), ("E", 1), ("D", 1), ("D", 1), ("D",1), ("F", 1), ("E",1), ("E",1), ("D",1), ("D",1), ("C", 2)]
        for nuotti in nuotit:
            musicalbeeps.Player(volume = 1, mute_output = False).play_note(nuotti[0], nuotti[1])
        print("soitin ukko-nooan ;)")

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
        self._nakymaNyt.pakkaa()

ikkuna = Tk()
ikkuna.title("tiralabra")

kayttoliittyma = KL(ikkuna)
kayttoliittyma.aloita()

ikkuna.mainloop()
