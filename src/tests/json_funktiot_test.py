import unittest
from json_funktiot import avaa_json, tallenna_json

class Test_json_funktiot(unittest.TestCase):
    """Testiluokka, joka testaa json-funktioita
    """
    def setUp(self):
        """Testiluokan alustusmetodi
        """
        pass

    def test_avaa_json_antaa_dictionaryn(self):
        """Testimetodi, joka testaa, että avaa_json-funktio antaa data.json-tiedostossa
        olevan tiedon dictionarynä.
        """
        data = avaa_json()
        self.assertEqual(type(data) is dict, True)
        avaimet = list(data.keys())
        self.assertEqual(["nuotit", "savelet"], avaimet)

    def test_tallenna_json_tallentaa_oikein(self):
        """Testimetodi, joka testaa, että tallenna_json-funktio korvaa data.json-tiedoston
        nykyisen sisällön argumenttinä annetulla sisällöllä
        """
        dataAlussa = avaa_json()
        tallennettava = {"nuotit": ["1"], "savelet": ["C4"]}
        tallenna_json(tallennettava)
        dataLopussa = avaa_json()
        self.assertNotEqual(dataAlussa, dataLopussa)
        tallenna_json(dataAlussa)



