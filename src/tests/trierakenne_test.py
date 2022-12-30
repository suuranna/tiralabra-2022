import unittest
from trierakenne import TrieRakenne
from json_funktiot import avaa_json
from kappaleen_generoiminen import generoi_kappale

class TestTrierakenne(unittest.TestCase):
    """Testiluokka, joka testaa TrieRakenne-luokkaa
    """
    def setUp(self):
        """Testiluokan alustusmetodi
        """
        self.trie = TrieRakenne("sävelet")
        self.trie2 = TrieRakenne("nuotit")
        self.data_alussa = avaa_json()

    def test_luo_Trierakenne(self):
        """Testimetodi, joka testaa, että uuden TrieRakenne-olion luonti onnistuu
        """
        self.assertEqual(self.trie.savelet_vai_nuotit, "sävelet")
        self.assertEqual(self.trie2.savelet_vai_nuotit, "nuotit")
        self.assertEqual(self.trie.alku.nimi, "")
        self.assertEqual(self.trie2.alku.nimi, "")
        self.assertEqual(self.trie.pisin, 0)
        self.assertEqual(self.trie2.pisin, 0)
        self.assertEqual(self.trie.alku.lapset, {})
        self.assertEqual(self.trie2.alku.lapset, {})

    def test_trierakenteen_pisin_on_opetusdatan_pisimmän_kappaleen_pituus(self):
        """Testimetodi, joka testaa, että self.pisin on sama kuin opetusdatan
        pisimmän kappaleen pituus
        """
        data = avaa_json()
        pisinS = 0
        pisinN = 0

        for kappale in data["nuotit"]:
            if len(kappale) > pisinN:
                pisinN = len(kappale)

        for kappale in data["savelet"]:
            if len(kappale) > pisinS:
                pisinS = len(kappale)

        self.trie.lisaa_opetusdata_trieen(3)
        self.trie2.lisaa_opetusdata_trieen(3)
        self.assertEqual(pisinN, self.trie2.pisin)
        self.assertEqual(pisinS, self.trie.pisin)
            
    def test_generoidun_kappaleen_pituus_on_0_ja_pisimmän_opetuskappaleen_pituuden_välistä(self):
        """Testimetodi, joka testaa, että generoi_kappale-funktio pystyy generoimaan kappaleen
        kaikilla pituuksilla, jotka ovat 2:n ja opetusdatan pisimmän kappaleen pituuden välistä.
        """
        pisin = 0
        for kappale in self.data_alussa["savelet"]:
            if len(kappale) > pisin:
                pisin = len(kappale)
        
        for i in range(2, pisin + 1):
            kappale = generoi_kappale(1, i, "sävelet")
            self.assertEqual(len(kappale), i)
        #self.assertEqual(self.trie2.luo_kappale(self.trie2.pisin + 1, self.trie2.pisin + 1), None)

    def test_generoi_kappale_palauttaa_listan(self):
        """Testimetodi, joka testaa, että generoi_kappale-funktio palauttaa listan onnistuneen
        luonnin seurauksena
        """
        kappale = generoi_kappale(4, 5, "säveliä")
        self.assertTrue(isinstance(kappale, list))

