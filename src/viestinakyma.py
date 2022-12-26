from tkinter import Tk, Text, ttk
from nakyma import Nakyma

class Viestinakyma(Nakyma):
    """Luokka, joka näyttää halutun viestin uutena ikkunana
    ja jonka yläluokka on luokka Nakyma
    
    Attributes:
        juuri: juurikomponentti
    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden viestinäkymän omassa ikkunassa
        """
        super().__init__(Tk())
        self.kehys = self.juuri
        self.juuri.title("Viesti")

    def nayta_viesti(self, viesti):
        """Luo viestinäkymän komponentit ja näyttää viesti-ikkunassa argumenttinä annetun viestin
        Args:
            viesti: String-muodossa oleva viesti, joka halutaan näyttää
                käyttäjälle viesti-ikkunassa
        """
        otsikko = ttk.Label(
            master=self.juuri,
            text="Viesti")
        teksti = Text(
            master=self.juuri,
            height=5,
            width=30)
        teksti.insert('1.0', viesti)
        otsikko.pack()
        teksti.pack()
