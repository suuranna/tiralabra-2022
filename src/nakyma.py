from tkinter import constants

class Nakyma:
    def __init__(self, juuri):
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
