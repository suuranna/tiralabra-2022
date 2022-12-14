from collections import deque
from trierakenne import TrieRakenne
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
        return "Aste voi korkeintaan olla yhden pienempi kuin opetusdatan pisin kappale." + \
               "Tällä hetkellä korkein mahdollinen aste on: " + str(trie.pisin)

    kappale = None

    try:
        kappale = etsi_seuraava(pituus, aste, [], trie, deque([]))
    except RecursionError:
        return "Kappaleen generoiminen ei onnistunut. " + \
               "Kokeile generointia esimerkiksi pienemmällä pituudella"

    if kappale is None:
        return "Kappaleen generoiminen ei onnistunut. " + \
               "Kokeile generointia esimerkiksi pienemmällä asteella"

    return kappale

def etsi_seuraava(pituus, aste, kappale, trie, edelliset):
    """Rekursiivinen funktio, joka etsii kappaleelle seuraavia
    nuotteja/säveliä niin kauan kunnes kappale on halutun pituinen

    Args:
        pituus: kappaleen haluttu pituus
        aste: määrittää, kuinka monta edellistä säveltä/nuottia määrittää seuraavan
            sävelen/nuotitn
        kappale: lista jo valituista sävelistä/nuoteista
        trie: trie-rakenne, jossa on määriteltynä sävel- tai nuottisekvenssejä
        edelliset: jono kappaleen viimeisistä sävelistä/nuoteista

    """
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
        generoitu_kappale = etsi_seuraava(pituus, aste, kappale, trie, edelliset)
        if isinstance(generoitu_kappale, list):
            return generoitu_kappale
        aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste)
    aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste)

def aseta_uudet_kappale_ja_edelliset(kappale, edelliset, aste):
    """Funktio, joka poistaa kappaleen viimeisen alkion ja päivittää
    edelliset vastaamaan kappaleen viimeisiä alkioita

    Args:
        kappale: lista, joka koostuu sävelistä/nuoteista
        edelliset: jono, joka koostuu kappaleen viimeisistä alkioista
        aste: määrittää, kuinka monta edellistä säveltä/nuottia määrittää seuraavan
            sävelen/nuotitn
    """
    if len(kappale) > 0:
        kappale.pop()
    if len(edelliset) > 0:
        edelliset.pop()
    if len(kappale) - 1 - aste >= 0:
        edelliset.appendleft(kappale[len(kappale) - aste])
