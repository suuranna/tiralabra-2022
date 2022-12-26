import unittest
from trierakenne import TrieRakenne
from opetusdataan_datan_lisaaminen import lisaa_opetusdataan_kappale
from json_funktiot import avaaJson, tallennaJson

class Test_lisaa_opetusdataan_kappale(unittest.TestCase):
    def setUp(self):
        self.trie = TrieRakenne("sävelet")
        self.dataAlussa = avaaJson()
        self.lisattava = "C4-1/8 D4-1/2 C4#-1/8 D4b-1/8"

        self.trie.alusta()

    def test_onnistuneen_lisayksen_seurauksena_metodi_palauttaa_tuplen(self):
        savelet_ja_nuotit = lisaa_opetusdataan_kappale(self.lisattava)
        self.assertTrue(isinstance(savelet_ja_nuotit, tuple))
        tallennaJson(self.dataAlussa)

    def test_opetusdataan_lisatty_kappale_tallentuu_json_tiedostoon(self):
        lisatty = lisaa_opetusdataan_kappale(self.lisattava)
        data_lisayksen_jalkeen = avaaJson()
        self.assertEqual(len(data_lisayksen_jalkeen["savelet"]), len(self.dataAlussa["savelet"]) + 1)
        self.assertEqual(len(data_lisayksen_jalkeen["nuotit"]), len(self.dataAlussa["nuotit"]) + 1)
        self.assertTrue(lisatty[0] in data_lisayksen_jalkeen["savelet"])
        self.assertTrue(lisatty[1] in data_lisayksen_jalkeen["nuotit"])

        tallennaJson(self.dataAlussa)
        