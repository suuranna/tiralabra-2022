from tkinter import Tk, ttk
from aloitusNakyma import AloitusNakyma
from kappaleNakyma import KappaleNakyma
from opetus_nakyma import OpetusNakyma
from kappaleen_luonti import *
from jsonFunktiot import *
from trierakenne import *

class KL:
    """Luokka, joka vastaa käyttöliittymää

    Attributes:
        _juuri: juurikomponentti
        _nakymaNyt: tämänhetkinen näkymä
        _uudenKappaleenSavelet: uusimman generoidun kappaleen sävelet
        _uudenKappaleenNuotit: uusimman generoidun kappaleen nuotit
        _tempo: kappaleen tempo 


    """
    def __init__(self, juuri):
        self._juuri = juuri
        self._nakymaNyt = None
        self._savelet = TrieRakenne("sävelet")
        self._nuotit = TrieRakenne("nuotit")
        #self._tempo = None
        

    def aloita(self):
        self.nayta_etusivu()

    def piilota_nakyma(self):
        """Piilottaa tämänhetkisen näkymän, jotta tilalle voidaan laittaa uusi näkymä
        """
        if self._nakymaNyt:
            self._nakymaNyt.tuhoa()

        self._nakymaNyt = None

    def lisaa_opetusdataa(self):
        """Lisää opetusdataan -napin tapahtumakäsittelijä, jonka on tarkoitus lisätä kirjoitettu kappale opetusdataan
        """
        print("tätä toimintoa ei ole vielä ohjelmoitu")

    def siirry_kappalenakymaan(self):
        self.nayta_generoitu_kappale()

    def siirry_etusivulle(self):
        self.nayta_etusivu()

    def siirry_opetusdatan_lisaamiseen(self):
        self.nayta_opetusnakyma()

    def nayta_opetusnakyma(self):
        self.piilota_nakyma()
        self._nakymaNyt = OpetusNakyma(self._juuri, self.lisaa_opetusdataa, self.siirry_etusivulle)
        self._nakymaNyt.pakkaa()

    def nayta_generoitu_kappale(self):
        """Generoi uuden kappaleen ja laittaa tämänhetkiseksi näkymäksi näkymän, 
        jossa voi soittaa generoidun kappaleen
        """
        #self._uudenKappaleenSavelet = arvo_savelia()
        #self._uudenKappaleenNuotit = arvo_nuotteja()
        self.piilota_nakyma()
        self._nakymaNyt = KappaleNakyma(self._juuri, self.siirry_etusivulle, self._nuotit, self._savelet)
        #self._nakymaNyt = KappaleNakyma(self._juuri, self.soita_generoitu_kappale, self.siirry_etusivulle)
        #self._nakymaNyt = KappaleNakyma(self._juuri, self.siirry_etusivulle, self.soita_generoitu_kappale, self._tempo)
        self._nakymaNyt.pakkaa()

    def nayta_etusivu(self):
        """Laittaa tämänhetkiseksi näkymäksi etusivun
        """
        self.piilota_nakyma()

        self._nakymaNyt = AloitusNakyma(self._juuri, self.siirry_kappalenakymaan, self.siirry_opetusdatan_lisaamiseen)
        self._nakymaNyt.pakkaa()

