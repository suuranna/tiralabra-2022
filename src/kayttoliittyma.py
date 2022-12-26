from aloitusnakyma import Aloitusnakyma
from kappalenakyma import Kappalenakyma
from opetusnakyma import Opetusnakyma
from trierakenne import TrieRakenne

class KL:
    """Luokka, joka vastaa käyttöliittymää

    Attributes:
        juuri: juurikomponentti
        nakyma_nyt: tämänhetkinen näkymä
        savelet: Trierakenne, joka koostuu opetusdatan sävelsekvensseistä
        nuotit: Trierakenne, joka koostuu opetusdatan nuottisekvensseistä

    """

    def __init__(self, juuri):
        """Luokan konstruktori, joka luo uuden käyttöliittymän (KL:n)

        Args:
            juuri: juurikomponentti
        """
        self.juuri = juuri
        self.nakyma_nyt = None
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
        if self.nakyma_nyt:
            self.nakyma_nyt.tuhoa()

        self.nakyma_nyt = None

    def siirry_kappalenakymaan(self):
        """Metodi, joka kutsuu halutun näkymän, eli tässä tilanteessa
        kappalenäkymän, näyttävää metodia
        """
        self.nayta_generoitu_kappale()

    def siirry_etusivulle(self):
        """Metodi, joka kutsuu halutun näkymän, eli tässä tilanteessa
        etusivun, näyttävää metodia
        """
        self.nayta_etusivu()

    def siirry_opetusdatan_lisaamiseen(self):
        """Metodi, joka kutsuu halutun näkymän, eli tässä tilanteessa
        opetusnäkymän, näyttävää metodia
        """
        self.nayta_opetusnakyma()

    def nayta_opetusnakyma(self):
        """Luo opetusnäkymän, jossa voi lisätä kappaleita
        opetusdataan, ja laittaa sen tämänhetkiseksi näkymäksi
        """
        self.piilota_nakyma()
        self.nakyma_nyt = Opetusnakyma(
            self.juuri,
            self.siirry_etusivulle,
            self.savelet,
            self.nuotit)
        self.nakyma_nyt.pakkaa()

    def nayta_generoitu_kappale(self):
        """Luo kappalenäkymän, jossa voi kuunnella
        generoidun kappaleen, ja laittaa sen tämänhetkiseksi näkymäksi
        """
        self.piilota_nakyma()
        self.nakyma_nyt = Kappalenakyma(
            self.juuri,
            self.siirry_etusivulle,
            self.nuotit,
            self.savelet)
        self.nakyma_nyt.pakkaa()

    def nayta_etusivu(self):
        """Laittaa tämänhetkiseksi näkymäksi etusivun
        """
        self.piilota_nakyma()
        self.nakyma_nyt = Aloitusnakyma(
            self.juuri,
            self.siirry_kappalenakymaan,
            self.siirry_opetusdatan_lisaamiseen)
        self.nakyma_nyt.pakkaa()
