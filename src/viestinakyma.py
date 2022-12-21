from tkinter import Tk, Text, ttk

class Viestinakyma:
    """Luokka, joka näyttää halutun viestin uutena ikkunana

    Attributes:
        juuri: juurikomponentti

    """
    def __init__(self):
        """Luokan konstruktori, joka luo uuden viestinäkymän omassa ikkunassa
        
        """
        self.juuri = Tk()
        self.juuri.title("Viesti")
        
    def tuhoa(self):
        """Tuhoaa viesti-ikkunan, jolloin se poistuu näkyvistä
        
        """
        self.juuri.destroy()

    def nayta_viesti(self, viesti):
        """Luo viestinäkymän komponentit ja näyttää viesti-ikkunassa argumenttinä annetun viestin

        Args:
            viesti: String-muodossa oleva viesti, joka halutaan näyttää käyttäjälle viesti-ikkunassa
        
        """
        otsikko = ttk.Label(master=self.juuri, text="Viesti")
        teksti = Text(master=self.juuri, height=5, width=30)
        teksti.insert('1.0', viesti)
        otsikko.pack()
        teksti.pack()
