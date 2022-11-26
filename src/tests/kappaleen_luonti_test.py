import unittest
from kappaleen_luonti import *

class TestKappaleen_luonti(unittest.TestCase):
    def setUp(self):
        print("testi")

    def test_arvo_savelia(self):
        savelet = arvo_savelia()
        self.assertEqual(15, len(savelet))

    def test_arvo_nuotteja(self):
        nuotteja = arvo_nuotteja()
        self.assertEqual(15, len(nuotteja))
