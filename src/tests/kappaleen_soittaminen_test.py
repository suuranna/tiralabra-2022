import unittest
from kappaleen_soittaminen import soita_kappale
from soittaja import Soittaja

class Test_kappaleen_soittaminen(unittest.TestCase):
    def setUp(self):
        self.savelet = ["C4", "D4", "E4"]
        self.nuotit = ["1/4", "1/4", "1/2"]

    def test_soittaja_soittaa_savelen_halutulla_kestolla(self):
        soittaja = Soittaja()

        soittaja.soita("C4", 1)
        #self.assertEqual(soittaja is kappaleen_soittaminen.Soittaja, True)

    def test_soita_kappale_ei_soita_mitaan_jos_tempo_ei_kelpaa(self):
        soittaminen = soita_kappale(self.savelet, self.nuotit, -1)
        self.assertEqual(soittaminen, "Kirjoita jokin nollaa suurempi kokonaisluku numeromuodossa esim. 60")
        soittaminen = soita_kappale(self.savelet, self.nuotit, "kuusikymmentä")
        self.assertEqual(soittaminen, "Kirjoita tempo numeromuodossa esim. 60")

    def test_soita_kappale_soittaa_kappaleen_jos_annetut_argumentit_kelpaavat(self):
        soittaminen = soita_kappale(self.savelet, self.nuotit, 500)
        self.assertEqual(soittaminen, 0)




