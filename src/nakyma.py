from tkinter import constants

class Nakyma:
    """Luokka, joka kuvaa näkymää käyttöliittymässä
    """
    def __init__(self, juuri):
        """Luokan konstruktori, joka luo uuden näkymän
        """
        self.juuri = juuri
        self.kehys = None

    def pakkaa(self):
        """Metodi, joka pakkaa näkymän visuaaliset komponentit
        """
        self.kehys.pack(fill=constants.X)

    def tuhoa(self):
        """Tuhoaa kappalenäkymän, jotta toinen näkymän voidaan laittaa tilalle
        """
        self.kehys.destroy()
