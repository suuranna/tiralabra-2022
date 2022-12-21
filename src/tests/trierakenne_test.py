import unittest
from trierakenne import *
from jsonFunktiot import *
from solmu import Solmu

class TestTrierakenne(unittest.TestCase):
    def setUp(self):
        self.trie = TrieRakenne("sävelet")
        self.trie2 = TrieRakenne("nuotit")

        self.trie.alusta()
        self.trie2.alusta()

    def test_luo_Trierakenne(self):
        self.assertEqual(self.trie.savelet_vai_nuotit, "sävelet")
        self.assertEqual(self.trie2.savelet_vai_nuotit, "nuotit")
        self.assertEqual(self.trie.alku.nimi, "")
        self.assertEqual(self.trie2.alku.nimi, "")

    def test_alusta_metodi_alustaa_oikein(self):
        trie = TrieRakenne("sävelet")
        self.assertEqual(trie.pisin, 0)
        self.assertEqual(trie.alku.lapset, {})

        trie.alusta()

        pisin = 0
        data = avaaJson()
        savelet = []

        for kappale in data["savelet"]:
            if len(kappale) > pisin:
                pisin = len(kappale)
            for savel in kappale:
                if savel not in savelet:
                    savelet.append(savel)

        self.assertEqual(pisin, trie.pisin)
        self.assertNotEqual(trie.alku.lapset, {})
        self.assertEqual(savelet, list(trie.alku.lapset.keys()))


    def test_kappaletta_ei_generoida_vaaranlaisilla_minilla_ja_maxilla(self):
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], 0, 0), None)
        self.assertEqual(self.trie2.generoi_kappale(self.trie2.alku, [], 0, 0), None)
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], 10, 1), None)
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], -10, 0), None)
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], 0, -10), None)

    def test_trierakenteen_pisin_on_opetusdatan_pisimmän_kappaleen_pituus(self):
        data = avaaJson()
        pisinS = 0
        pisinN = 0

        for kappale in data["nuotit"]:
            if len(kappale) > pisinN:
                pisinN = len(kappale)

        for kappale in data["savelet"]:
            if len(kappale) > pisinS:
                pisinS = len(kappale)

        self.assertEqual(pisinN, self.trie2.pisin)
        self.assertEqual(pisinS, self.trie.pisin)
            

    def test_generoidun_kappaleen_pituus_on_0_ja_pisimmän_opetuskappaleen_pituuden_välistä(self):
        pisin = self.trie2.pisin
        
        for i in range(1, pisin):
            kappale = self.trie2.luo_kappale(i, i)
            self.assertEqual(len(kappale), i)

    def test_luo_kappale_palauttaa_listan_tai_none(self):
        kappale = self.trie.luo_kappale(5, 5)
        self.assertTrue(isinstance(kappale, list))

        

class TestSolmu(unittest.TestCase):
    def setUp(self):
        pass

    def test_solmun_luonti(self):
        solmu = Solmu("C4")
        self.assertEqual(solmu.nimi, "C4")
        self.assertEqual(len(list(solmu.lapset.keys())), 0)
        self.assertEqual(solmu.maara, 1)
        self.assertEqual(solmu.kappaleen_loppu, False)