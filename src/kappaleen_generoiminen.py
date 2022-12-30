from trierakenne import TrieRakenne
from collections import deque
from arpoja import Arpoja

def generoi_kappale(aste, pituus, savelia_vai_nuotteja):
    """Funktio, joka generoi uuden kappaleen, joka koostuu
    joko nuoteista tai sävelistä, ja palauttaa sen listana

    Args:
        aste: Markovin ketjun aste, joka määrittää, kuinka monta
            edellistä nuottia/säveltä määrittää seuraavan nuotin/sävelen
        pituus: määrittää, kuinka pitkä kappale generoidaan
        savelia_vai_nuotteja: määrittää generoidaanko nuotti- vai
            sävelsekvenssejä

    Returns:
        String, jos aste tai pituus ei ollut oikeassa muodossa
        Lista, jos kappaleen generoiminen meni niin kuin piti
    """
    try:
        aste = int(aste)
    except ValueError:
        return "Kirjoita aste numeromuodossa esim. 10"
    
    try:
        pituus = int(pituus)
    except ValueError:
        return "Kirjoita pituus numeromuodossa esim. 10"

    if pituus < 2:
        return "Valitse kappaleen pituudeksi luku, joka on vähintään 2"

    if aste < 1:
        return "Valitse aste, joka on vähintään 1"

    if aste > pituus - 1:
        return "Valitse aste, joka on pienempi kuin valisemasi pituus"
    
    trie = TrieRakenne(savelia_vai_nuotteja)
    trie.lisaa_opetusdata_trieen(aste)

    if aste > trie.pisin - 1:
        return "Aste voi korkeintaan olla yhden pienempi kuin opetusdatan pisin kappale. Tällä hetkellä korkein mahdollinen aste on: " + str(trie.pisin)
    kappale = None
    try:
        kappale = rekursio(pituus, aste, [], trie, deque([]))
    except RecursionError:
        pass

    if kappale == None:
        return "Kappaleen generoiminen ei onnistunut. Kokeile generointia toisilla arvoilla"

    return kappale

def rekursio(pituus, aste, kappale, trie, edelliset):
    """Rekursiivinen funktio, joka etsii kappaleelle seuraavia
    nuotteja/säveliä
    """
    if len(kappale) == pituus:
        return kappale
    arpoja = Arpoja()

    seuraajat = trie.etsi_sekvenssin_seuraajat(edelliset)

    while len(seuraajat[0]) > 0:
        seuraaja = arpoja.arvo(seuraajat[0], seuraajat[1])

        for i in range(len(seuraajat[0])):
            if seuraajat[0][i] == seuraaja:
                seuraajat[0].pop(i)
                seuraajat[1].pop(i)
                break

        kappale.append(seuraaja)
        if len(edelliset) == aste:
            edelliset.popleft()
        edelliset.append(seuraaja)

        if len(kappale) == pituus:
            return kappale

        if not isinstance(trie.etsi_sekvenssin_seuraajat(edelliset), tuple):
            aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste)
            continue

        if len(kappale) >= pituus:
            return kappale
        generoitu_kappale = rekursio(pituus, aste, kappale, trie, edelliset)
        if isinstance(generoitu_kappale, list):
            return generoitu_kappale
        aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste)
    aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste)

def aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste):
    if len(kappale) > 0:
        kappale.pop()
    if len(edelliset) > 0:
        edelliset.pop()
    if len(kappale) - 1 - aste >= 0:
        edelliset.appendleft(kappale[len(kappale) - aste])


