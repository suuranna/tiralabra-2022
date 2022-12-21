import random

class Arpoja:
    """Luokka, jolla vältetään konkreettinen riippuvuus randomiin

    """
    def __init__(self):
        """Luoka konstruktori, joka luo uuden arpojan

        """
        pass

    def arvo(self, lista, todennakoisyydet):
        """Arpoo annetusta listasta alkion annettujen todennäköisyyskien perusteella

        Args:
            lista: lista alkioita, joista arvotaan yksi
            todennäköisyydet: listan alkioiden todennäköisyydet
        
        """
        arvottu = random.choices(lista, weights=todennakoisyydet)
        return arvottu[0]