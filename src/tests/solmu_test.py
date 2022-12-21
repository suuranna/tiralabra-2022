import unittest
from solmu import Solmu

class TestSolmu(unittest.TestCase):
    def setUp(self):
        pass

    def test_solmun_luonti(self):
        solmu = Solmu("C4")
        self.assertEqual(solmu.nimi, "C4")
        self.assertEqual(len(list(solmu.lapset.keys())), 0)
        self.assertEqual(solmu.maara, 1)
        self.assertEqual(solmu.kappaleen_loppu, False)