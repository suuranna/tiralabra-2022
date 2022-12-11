from tkinter import Tk, Text, ttk

class Viestinakyma:
    """Luokka, joka näyttää halutun viestin uutena ikkunana

    Attributes:
        _juuri: juurikomponentti

    """
    def __init__(self):
        self._juuri = Tk()
        self._juuri.title("Viesti")
        
    def tuhoa(self):
        self._juuri.destroy()

    def nayta_viesti(self, viesti):
        otsikko = ttk.Label(master=self._juuri, text="Viesti")
        teksti = Text(master=self._juuri, height=5, width=30)
        teksti.insert('1.0', viesti)
        otsikko.pack()
        teksti.pack()
