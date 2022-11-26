import random
import musicalbeeps
from jsonFunktiot import avaaJson#, tallennaJson

def arvo_savelia():
    notes = []
    data = avaaJson()
    savelet = data["sävelet"]
    savelia = list(savelet.keys())
    alku = random.choice(savelia)

    edellinen = alku
    for i in range(15):
        savelet2 = None
        todennakoisyys = []
        if i == 0:
            notes.append(edellinen)
            continue
        savelet2 = list(savelet[edellinen].keys())
        for savel in savelet2:
            todennakoisyys.append(savelet[edellinen][savel])
        savel = random.choices(savelet2, weights=todennakoisyys, k=1)
        notes.append(savel[0])
        edellinen = savel[0]
    return notes
        
def arvo_nuotteja():
    notes = []
    data = avaaJson()
    nuotit = data["nuotit"]

    nuotteja = ["neljäsosa", "puoli", "kahdeksasosa", "piste"]
    
    alku = random.choice(nuotteja)

    edellinen = alku
    for i in range(15):
        nuotit2 = None
        todennakoisyys = []
        if i == 0:
            notes.append(edellinen)
            continue
        nuotit2 = list(nuotit[edellinen].keys())
        for nuotti in nuotit2:
            todennakoisyys.append(nuotit[edellinen][nuotti])
        nuotti = random.choices(nuotit2, weights=todennakoisyys, k=1)
        notes.append(nuotti[0])
        edellinen = nuotti[0]

    return notes

def lisaa_kappale_opetusdataan(kappale):
    """Lisää annetun kappaleen opetusdataan
    Kesken
    """
    lista = kappale.split()
    edellinenNuotti = None
    edellinenSavel = None
    if len(lista) <= 1:
        return "Anna kappale, joka on pidempi kuin yksi nuotti/sävel"

    for alkio in lista:
        eroteltu = alkio.split("-")
        if len(eroteltu) != 2 or len(eroteltu[0]) != 2 or len(eroteltu[1]) != 1:
            return "Annettu kappale ei ollut kirjoitettu oikeassa muodossa"
        if edellinenNuotti == None and edellinenSavel == None:
            edellinenNuotti = eroteltu[1]
            edellinenSavel = eroteltu[0]
            continue
        # lisää eroteltu[0] edellisen savelen dictionaryyn kasvattamalla sitä yhdellä
        # lisää nuotti eroteltu[1] edellisen nuotin dictionaryyn kasvattamalla sitä yhdellä
        if eroteltu[1] == "1":
            return
        elif eroteltu[1] == "2":
            return
        else: # elif eroteltu[1] == "3":
            return

    return "kappale lisätty onnistuneesti opetusdataan :)"

def soita_kappale(savelet, nuotit, tempo):
    for i in range(len(savelet)):
        kesto = 0
        if nuotit[i] == "neljäsosa":
            kesto = tempo / 60
        elif nuotit[i] == "puoli":
            kesto = tempo / 30
        elif nuotit[i] == "piste":
            kesto = tempo / 40
        else: # if kahdeksasosa
            kesto = tempo / 120
        musicalbeeps.Player(volume=1, mute_output=False).play_note(savelet[i], kesto)