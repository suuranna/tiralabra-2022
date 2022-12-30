import unittest
from kappaleen_generoiminen import generoi_kappale
from json_funktiot import avaa_json, tallenna_json
from opetusdataan_datan_lisaaminen import lisaa_opetusdataan_kappale
from trierakenne import TrieRakenne

class Test_generoi_kappale(unittest.TestCase):
    """Testiluokka, joka testaa generoi_kappale-funktiota
    """
    def setUp(self):
        """Testiluokan alustusmetodi
        """
        pass

    def test_generoi_kappale_ei_generoi_vaaranlaisilla_parametreilla(self):
        kappale = generoi_kappale("kuusi", 7, "sävelet")
        self.assertTrue(isinstance(kappale, str))
        kappale = generoi_kappale(4, "seitsemän", "sävelet")
        self.assertTrue(isinstance(kappale, str))
        kappale = generoi_kappale(4, 3, "sävelet")
        self.assertTrue(isinstance(kappale, str))
        kappale = generoi_kappale(0, 4, "sävelet")
        self.assertTrue(isinstance(kappale, str))
        kappale = generoi_kappale(4, 1, "sävelet")
        self.assertTrue(isinstance(kappale, str))

        opetusdata = avaa_json()
        pisin = 0
        for kappale in opetusdata["savelet"]:
            if len(kappale) > pisin:
                pisin = len(kappale)

        kappale = generoi_kappale(pisin, pisin + 5, "sävelet")
        self.assertTrue(isinstance(kappale, str))

    def test_generoitu_kappale_koostuu_opetusdatan_sekvensseista(self):
        for aste in range(1, 10):
            kappale = generoi_kappale(aste, 11, "sävelet")

            trie = TrieRakenne("sävelet")
            trie.lisaa_opetusdata_trieen(aste)
            for indeksi in range(len(kappale) - aste):
                sekvenssi = kappale[indeksi: indeksi + aste]
                seuraajat = trie.etsi_sekvenssin_seuraajat(sekvenssi)
                self.assertTrue(isinstance(seuraajat, tuple))

    """
    def test_generoi_kappale_sisältaa_asteen_mittaisia_patkia_opetusdatasta(self):
        data_alussa = avaa_json()
        tallenna_json({"nuotit": [], "savelet": []})
        lisaa_opetusdataan_kappale("A4-1/4 C4-1/4 C4-1/4 B4-1/4 C4-1/4 B4-1/4 B4-1/4 A4-1/4 C4-1/4 C4-1/4 B4-1/4 C4-1/4 B4-1/4 B4-1/4")
        data_nyt = avaa_json()
        sekvenssit = []
        for aste in range(1, 14):
            #for savel in data_nyt["savelet"][0]:
            for indeksi in range(len(data_nyt["savelet"][0]) - aste):
                sekvenssi = data_nyt["savelet"][0][indeksi: indeksi + aste]
                sekvenssit.append("".join(sekvenssi))

            kappale = generoi_kappale(aste, 19, "sävelet")
            for indeksi in range(len(kappale) - aste):
                sekvenssi = kappale[indeksi: indeksi + aste]
                sekvenssi_stringina = "".join(sekvenssi)
                self.assertTrue(sekvenssi_stringina in sekvenssit)
        
        tallenna_json(data_alussa)

    """
    """
    def test_generoi_kappale_generoi_kappaleen_kaikilla_mahdollisilla_asteilla(self):
        opetusdata = avaa_json()
        pisin = 0
        for kappale in opetusdata["savelet"]:
            if len(kappale) > pisin:
                pisin = len(kappale)

        for aste in range(1, pisin):
            kappale = generoi_kappale(aste, pisin + 5, "sävelet")
            self.assertTrue(isinstance(kappale, list))
    """
