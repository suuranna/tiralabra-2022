import unittest
from trierakenne import TrieRakenne
from json_funktiot import avaa_json

class TestTrierakenne(unittest.TestCase):
    """Testiluokka, joka testaa TrieRakenne-luokkaa
    """
    def setUp(self):
        """Testiluokan alustusmetodi
        """
        self.trie = TrieRakenne("sävelet")
        self.trie2 = TrieRakenne("nuotit")

        self.trie.alusta()
        self.trie2.alusta()

    def test_luo_Trierakenne(self):
        """Testimetodi, joka testaa, että uuden TrieRakenne-olion luonti onnistuu
        """
        self.assertEqual(self.trie.savelet_vai_nuotit, "sävelet")
        self.assertEqual(self.trie2.savelet_vai_nuotit, "nuotit")
        self.assertEqual(self.trie.alku.nimi, "")
        self.assertEqual(self.trie2.alku.nimi, "")

    def test_alusta_metodi_alustaa_oikein(self):
        """Testimetodi, joka testaa, että alusta-metodi toimii halutusti
        """
        trie = TrieRakenne("sävelet")
        self.assertEqual(trie.pisin, 0)
        self.assertEqual(trie.alku.lapset, {})

        trie.alusta()

        pisin = 0
        data = avaa_json()
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


    def test_kappaletta_ei_generoida_vaaranlaisilla_minimilla_ja_maxksimilla(self):
        """Testimetodi, joka testaa, että generoi_kappale-metodi palauttaa None,
        jos minimi ja/tai maksimi on virheelliset
        """
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], 0, 0), None)
        self.assertEqual(self.trie2.generoi_kappale(self.trie2.alku, [], 0, 0), None)
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], 10, 1), None)
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], -10, 0), None)
        self.assertEqual(self.trie.generoi_kappale(self.trie.alku, [], 0, -10), None)

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
        self.assertEqual(pisinN, self.trie2.pisin)
        self.assertEqual(pisinS, self.trie.pisin)
            
    def test_generoidun_kappaleen_pituus_on_0_ja_pisimmän_opetuskappaleen_pituuden_välistä(self):
        """Testimetodi, joka testaa, että luo_kappale-metodi pystyy luomaan kappaleen
        kaikilla pituuksilla, jotka ovat 1:n ja opetusdatan pisimmän kappaleen pituuden välistä.
        """
        pisin = self.trie2.pisin
        
        for i in range(1, pisin + 1):
            kappale = self.trie2.luo_kappale(i, i)
            self.assertEqual(len(kappale), i)
        self.assertEqual(self.trie2.luo_kappale(self.trie2.pisin + 1, self.trie2.pisin + 1), None)

    def test_luo_kappale_palauttaa_listan(self):
        """Testimetodi, joka testaa, että luo_kappale-funktio palauttaa listan onnistuneen
        luonnin seurauksena
        """
        kappale = self.trie.luo_kappale(5, 5)
        self.assertTrue(isinstance(kappale, list))

    def test_luo_kappale_palauttaa_none_jos_minimi_ja_maksimi_on_virheelliset(self):
        """Testimetodi, joka testaa, että luo_metodi-funtio palauttaa None, jos minimi
        ja/tai maksimi ovat virheelliset
        """
        kappale = self.trie.luo_kappale(1, 100000000)
        self.assertEqual(kappale, None)
        kappale = self.trie.luo_kappale(100000000, 100000000)
        self.assertEqual(kappale, None)
        kappale = self.trie.luo_kappale(1000, 1)
        self.assertEqual(kappale, None)
        kappale = self.trie.luo_kappale(-1, 20)
        self.assertEqual(kappale, None)
        kappale = self.trie.luo_kappale(1, -100000)
        self.assertEqual(kappale, None)

