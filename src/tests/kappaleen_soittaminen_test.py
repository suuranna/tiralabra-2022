import unittest
from kappaleen_soittaminen import soita_kappale
from soittaja import Soittaja

class Test_kappaleen_soittaminen(unittest.TestCase):
    """Testiluokka, joka testaa kappaleen soittamista ja Soittaja-luokkaa"""
    def setUp(self):
        """Testiluoka alustusmetodi"""
        self.savelet = ["C4", "D4", "E4"]
        self.nuotit = ["1/4", "1/4", "1/2"]

    def test_soittaja_soittaa_savelen_halutulla_kestolla(self):
        """Testimetodi, joka testaa, että soittaja soittaa savelen halutulla kestolla
        """
        soittaja = Soittaja()

        soittaja.soita("C4", 1)

    def test_soita_kappale_ei_soita_mitaan_jos_tempo_ei_kelpaa(self):
        """Testimetodi, joka testaa, että soita_kappale_funktio ei soita mitään,
        jos käyttäjä antaa virheellisen tempon
        """
        soittaminen = soita_kappale(self.savelet, self.nuotit, -1)
        self.assertEqual(soittaminen, "Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60")
        soittaminen = soita_kappale(self.savelet, self.nuotit, "kuusikymmentä")
        self.assertEqual(soittaminen, "Kirjoita tempo numeromuodossa esim. 60")

    def test_soita_kappale_soittaa_kappaleen_jos_annetut_argumentit_kelpaavat(self):
        """Testimetodi, joka testaa, että soita_kappale-funktio palauttaa 1,
        jos se soittaa kappaleen onnistuneesti
        """
        soittaminen = soita_kappale(self.savelet, self.nuotit, 500)
        self.assertEqual(soittaminen, 0)




