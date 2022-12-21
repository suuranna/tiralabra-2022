from tkinter import Tk, ttk
from aloitusNakyma import AloitusNakyma
from kappaleNakyma import KappaleNakyma
from opetus_nakyma import OpetusNakyma
from kappaleen_soittaminen import *
from jsonFunktiot import *
from trierakenne import *

class KL:
    """Luokka, joka vastaa käyttöliittymää

    Attributes:
        juuri: juurikomponentti
        nakymaNyt: tämänhetkinen näkymä
        savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä 
        nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä

    """

    def __init__(self, juuri):
        """Luokan konstruktori, joka luo uuden käyttöliittymän (KL:n)

        Args:
            juuri: juurikomponentti

        """
        self.juuri = juuri
        self.nakymaNyt = None
        self.savelet = TrieRakenne("sävelet")
        self.nuotit = TrieRakenne("nuotit")

        self.savelet.alusta()
        self.nuotit.alusta()
        

    def aloita(self):
        """Käynnistää sovelluksen ja laittaa ensimmäiseksi näkymäksi etusivun

        """
        self.nayta_etusivu()

    def piilota_nakyma(self):
        """Piilottaa tämänhetkisen näkymän, jotta tilalle voidaan laittaa uusi näkymä

        """
        if self.nakymaNyt:
            self.nakymaNyt.tuhoa()

        self.nakymaNyt = None

    def siirry_kappalenakymaan(self):
        """Metodi, joka kutsuu halutun näkymän, eli tässä tilanteessa kappalenäkymän, näyttävää metodia

        """
        self.nayta_generoitu_kappale()

    def siirry_etusivulle(self):
        """Metodi, joka kutsuu halutun näkymän, eli tässä tilanteessa etusivun, näyttävää metodia

        """
        self.nayta_etusivu()

    def siirry_opetusdatan_lisaamiseen(self):
        """Metodi, joka kutsuu halutun näkymän, eli tässä tilanteessa opetusnäkymän, näyttävää metodia

        """
        self.nayta_opetusnakyma()

    def nayta_opetusnakyma(self):
        """Luo opetusnäkymän, jossa voi lisätä kappaleita opetusdataan, ja laittaa sen tämänhetkiseksi näkymäksi
        
        """  
        self.piilota_nakyma()
        self.nakymaNyt = OpetusNakyma(self.juuri, self.siirry_etusivulle, self.savelet, self.nuotit)
        self.nakymaNyt.pakkaa()

    def nayta_generoitu_kappale(self):
        """Luo kappalenäkymän, jossa voi kuunnella generoidun kappaleen, ja laittaa sen tämänhetkiseksi näkymäksi 

        """
        self.piilota_nakyma()
        self.nakymaNyt = KappaleNakyma(self.juuri, self.siirry_etusivulle, self.nuotit, self.savelet)
        self.nakymaNyt.pakkaa()

    def nayta_etusivu(self):
        """Laittaa tämänhetkiseksi näkymäksi etusivun

        """
        self.piilota_nakyma()
        self.nakymaNyt = AloitusNakyma(self.juuri, self.siirry_kappalenakymaan, self.siirry_opetusdatan_lisaamiseen)
        self.nakymaNyt.pakkaa()

