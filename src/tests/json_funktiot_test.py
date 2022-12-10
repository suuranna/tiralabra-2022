import unittest
from jsonFunktiot import *

class TestKappaleen_luonti(unittest.TestCase):
    def setUp(self):
        pass

    def test_avaaJson_antaa_dictionaryn(self):
        data = avaaJson()
        self.assertEqual(type(data) is dict, True)
        avaimet = list(data.keys())
        self.assertEqual(["nuotit", "savelet"], avaimet)

    def test_tallennaJson_tallentaa_oikein(self):
        dataAlussa = avaaJson()
        tallennettava = {"nuotit": ["1"], "savelet": ["C4"]}
        tallennaJson(tallennettava)
        dataLopussa = avaaJson()
        self.assertNotEqual(dataAlussa, dataLopussa)
        tallennaJson(dataAlussa)



