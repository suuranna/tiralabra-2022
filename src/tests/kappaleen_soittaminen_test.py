import unittest
from kappaleen_soittaminen import *

class Test_kappaleen_luonti(unittest.TestCase):
    def setUp(self):
        pass

    def test_soittaja(self):
        soittaja = Soittaja()

        soittaja.soita("C4", 1)
        #self.assertEqual(soittaja is kappaleen_soittaminen.Soittaja, True)
