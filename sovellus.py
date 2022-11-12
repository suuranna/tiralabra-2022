from tkinter import Tk, ttk
import musicalbeeps


class KL:
    def __init__(self, juuri):
        self._juuri = juuri

    def aloita(self):
        otsikko = ttk.Label(master=self._juuri, text="musiikin tuottaja")
        nappi = ttk.Button(master=self._juuri, text="soita ukko-nooa", command=self.napin_painaminen)

        otsikko.pack()
        nappi.pack()

    def napin_painaminen(self):
        nuotit = [("C", 1), ("C", 1), ("C", 1), ("E", 1), ("D", 1), ("D", 1), ("D",1), ("F", 1), ("E",1), ("E",1), ("D",1), ("D",1), ("C", 2)]
        for nuotti in nuotit:
            musicalbeeps.Player(volume = 1, mute_output = False).play_note(nuotti[0], nuotti[1])
        print("soitin ukko-nooan ;)")

        uusi_nappi = ttk.Button(master=self._juuri, text="olen uusi nappi")
        uusi_nappi.pack()

ikkuna = Tk()
ikkuna.title("tiralabra")

kayttoliittyma = KL(ikkuna)
kayttoliittyma.aloita()

ikkuna.mainloop()
