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
    
    def test_etsi_sekvenssin_seuraajat_loytaa_oikeat_seuraajat(self):
        """Testimetodi, joka testaa, että etsi_sekvenssin_seuraajat-metodi
        löytää oikeat seuraajat
        """
        kappale = ["A4", "C4", "C4", "B4", "C4", "B4", "B4"]

        self.trie.lisaa_kappale(2, kappale)

        seuraajat = self.trie.etsi_sekvenssin_seuraajat(["C4", "B4"])
        self.assertEqual(seuraajat[0], ["C4", "B4"])

        seuraajat = self.trie.etsi_sekvenssin_seuraajat(["C4"])
        self.assertEqual(seuraajat[0], ["C4", "B4"])

        seuraajat = self.trie.etsi_sekvenssin_seuraajat([])
        self.assertEqual(seuraajat[0], ["A4", "C4", "B4"])

        seuraajat = self.trie.etsi_sekvenssin_seuraajat(["A4", "C4", "C4"])
        self.assertEqual(seuraajat[0], [])

        seuraajat = self.trie.etsi_sekvenssin_seuraajat(["A4", "C4", "C4", "B4"])
        self.assertTrue(isinstance(seuraajat[0], str))
