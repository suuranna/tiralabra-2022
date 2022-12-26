import unittest
from syotetyn_kappaleen_tarkistus import syotetyn_kappaleen_tarkistus

class Test_syotetyn_kappaleen_tarkistus(unittest.TestCase):
    def setUp(self):
        pass

    def test_oikein_kirjoitettu_kappale_palauttaa_1(self):
        tarkistus = syotetyn_kappaleen_tarkistus("C4-1/4 G4-1/4 D4-1/4 E4-1/2")
        self.assertEqual(1, tarkistus)

    def test_yhden_saveln_mittaista_kappaletta_ei_hyvaksyta(self):
        tarkistus = syotetyn_kappaleen_tarkistus("C4-1/2")
        self.assertEqual("Anna kappale, joka on pidempi kuin yksi nuotti/sävel", tarkistus)

    def test_vaarin_kirjoitettua_kappaletta_ei_hyvaksyta(self):
        tarkistus = syotetyn_kappaleen_tarkistus("Ä41/8 ok-1")
        self.assertEqual("Annettu kappale ei ollut kirjoitettu oikeassa muodossa", tarkistus)

    def test_sallituiden_nuottien_ulkopuolella_olevaa_savelta_ei_hyvaksyta(self):
        tarkistus = syotetyn_kappaleen_tarkistus("C4-1/2 G4#-1 M4-1/8")
        self.assertEqual("Joku sävelistä ei ollut oikeassa muodossa", tarkistus)

    def test_sallituiden_nuottien_ulkopuolella_olevaa_nuottia_ei_hyväksyta(self):
        tarkistus = syotetyn_kappaleen_tarkistus("C4-1/2 D4-1/2 C4-1/3")
        self.assertEqual("Joku nuoteista ei ollu oikeassa muodossa", tarkistus)

    def test_vaaranlaista_ylennys_tai_alennus_merkkia_ei_hyvaksyta(self):
        tarkistus = syotetyn_kappaleen_tarkistus("C4-1/2 D4-1 G4%-1/2")
        self.assertEqual("Vääränlainen ylennys- tai alennusmerkki", tarkistus)
        tarkistus = syotetyn_kappaleen_tarkistus("C4-1/2 D4-1 B4B-1/2")
        self.assertEqual("Vääränlainen ylennys- tai alennusmerkki", tarkistus)