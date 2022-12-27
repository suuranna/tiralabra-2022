import unittest
from trierakenne import TrieRakenne
from opetusdataan_datan_lisaaminen import lisaa_opetusdataan_kappale
from json_funktiot import avaa_json, tallenna_json

class Test_lisaa_opetusdataan_kappale(unittest.TestCase):
    """Testiluokka, joka testaa lisaa_opetusdataan_kappale-funktiota
    """
    def setUp(self):
        """Testiluokan alustusmetodi
        """
        self.trie = TrieRakenne("sävelet")
        self.dataAlussa = avaa_json()
        self.lisattava = "C4-1/8 D4-1/2 C4#-1/8 D4b-1/8"

        self.trie.alusta()

    def test_onnistuneen_lisayksen_seurauksena_metodi_palauttaa_tuplen(self):
        """Testimetodi, joka testaa, että oikein kirjoitetun kappaleen lisääminen
        opetusdataan palauttaa tuplen
        """
        savelet_ja_nuotit = lisaa_opetusdataan_kappale(self.lisattava)
        self.assertTrue(isinstance(savelet_ja_nuotit, tuple))
        tallenna_json(self.dataAlussa)

    def test_epaonnistuneet_lisayksen_seurauksena_metodi_palauttaa_stringin(self):
        """Testimetodi, joka testaa, että epäonnistuneen lisäyksen seurauksena
        funktio palauttaa virheviestin stringinä
        """
        savelet_ja_nuotit = lisaa_opetusdataan_kappale("C4-1/8 D4-/2 C4#-1/8 D4b-1/8")
        self.assertTrue(isinstance(savelet_ja_nuotit, str))
        tallenna_json(self.dataAlussa)        

    def test_opetusdataan_lisatty_kappale_tallentuu_json_tiedostoon(self):
        """Testimetodi, joka testaa, että lisaa_opetusdataan_kappale-funktio
        tallentaa oikein kirjoitetun kappaleen data.json-tiedostoon
        """
        lisatty = lisaa_opetusdataan_kappale(self.lisattava)
        data_lisayksen_jalkeen = avaa_json()
        self.assertEqual(len(data_lisayksen_jalkeen["savelet"]), len(self.dataAlussa["savelet"]) + 1)
        self.assertEqual(len(data_lisayksen_jalkeen["nuotit"]), len(self.dataAlussa["nuotit"]) + 1)
        self.assertTrue(lisatty[0] in data_lisayksen_jalkeen["savelet"])
        self.assertTrue(lisatty[1] in data_lisayksen_jalkeen["nuotit"])

        tallenna_json(self.dataAlussa)

    def test_savel_H_muuttuu_saveliksi_B(self):
        """Testimetodi, joka testaa, että sävel H lisätään sävelenä B
        """
        trie = TrieRakenne("sävelet")
        tallenna_json({"nuotit": [], "savelet": []})
        kappale = "H4-1/4 H3b-1/4 H5#-1/4 B4-1/4"
        lisaa_opetusdataan_kappale(kappale)
        trie.alusta()
        generoitu_kappale = trie.luo_kappale(4, 4)
        self.assertEqual(generoitu_kappale, ["B4", "B3b", "B5#", "B4"])

        tallenna_json(self.dataAlussa)
        
    def tearDown(self) -> None:
        tallenna_json(self.dataAlussa)
        return super().tearDown()