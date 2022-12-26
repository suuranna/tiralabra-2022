import unittest
from arpoja import Arpoja

class Test_arpoja(unittest.TestCase):
    def setUp(self):
        self.arpoja = Arpoja()
        self.alkiot = ["C4", "D4", "E4"]

    def test_arpoja_arpoo_alkion_annetusta_listasta(self):
        arvottu = self.arpoja.arvo(self.alkiot, [1, 1, 1])
        self.assertTrue(arvottu in self.alkiot)

    def test_arpoja_ei_arvo_alkiota_jonka_todennakoisyys_on_0(self):
        onnistuiko = False
        for i in range(100):
            arvottu = self.arpoja.arvo(self.alkiot, [4, 10, 0])
            if arvottu == "E4":
                onnistuiko = True
        self.assertFalse(onnistuiko)

    

        