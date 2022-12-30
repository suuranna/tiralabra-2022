from tkinter import Tk
from kayttoliittyma import KL


ikkuna = Tk()
ikkuna.title("Musiikintuottaja")

kayttoliittyma = KL(ikkuna)
kayttoliittyma.aloita()

ikkuna.mainloop()
