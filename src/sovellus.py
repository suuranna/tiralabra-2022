from tkinter import Tk
from kayttoliittyma import KL


ikkuna = Tk()
ikkuna.title("tiralabra")

kayttoliittyma = KL(ikkuna)
kayttoliittyma.aloita()

ikkuna.mainloop()
