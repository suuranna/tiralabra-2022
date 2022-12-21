from jsonFunktiot import avaaJson, tallennaJson

def lisaa_opetusdataan_kappale(kappale):
    """Metodi, joka tarkistaa, että annettu kappale on oikeassa muodossa ja
    lisää sitten sen data.json-tiedostoon

    Args:
        kappale: String-muodossa opetusnäkymän tekstikenttään kirjoitettu kappale

    Returns:
        Jos annettu kappale on virheellisessä muodossa, palauttaa metodi String-muodossa viestejä.
        Jos kaikki menee niin kuin pitää ja kappale saadaan onnistuneesti lisättyä opetusdataan,
        palautetaan tuple, jossa on listana kirjoitetun kappaleen sävelet ja toisena listana nuotit
    
    """
    nuottien_vastaavuudet = {"1/4": "1", "1/8": "2", "1/2": "3", "3/8": "4", "1/16": "5", "1": "6", "3/16": "7"}
    sallitut_savelet = ["C", "D", "E", "F", "G", "A", "H", "B"]
    sallitut_oktaavit = ["3", "4", "5"]

    lista = kappale.split()
    savelet = []
    nuotit = []

    opetusdata = avaaJson()

    if len(lista) <= 1:
        return "Anna kappale, joka on pidempi kuin yksi nuotti/sävel" 

    for alkio in lista:
        eroteltu = alkio.split("-")
        if len(eroteltu) != 2 or len(eroteltu[0]) < 2 or len(eroteltu[0]) > 3:
            return "Annettu kappale ei ollut kirjoitettu oikeassa muodossa"
            
        if eroteltu[0][0] not in sallitut_savelet and eroteltu[0][1] not in sallitut_oktaavit:
            return "sävel ei ollut oikeassa muodossa"
    
        if eroteltu[1] not in nuottien_vastaavuudet.keys():
            return "nuotti ei ollu oikeassa muodossa"
            
        if len(eroteltu[0]) == 3:
            if eroteltu[0][2] == "#" or eroteltu[0][2] == "b":
                savelet.append(eroteltu[0])
                nuotit.append(nuottien_vastaavuudet[eroteltu[1]])
                continue
            else:
                return "Vääränlainen ylennys- tai alennusmerkki"

        savelet.append(eroteltu[0])
        nuotit.append(nuottien_vastaavuudet[eroteltu[1]])

    opetusdata["savelet"].append(savelet)
    opetusdata["nuotit"].append(nuotit)
    tallennaJson(opetusdata)
    return (savelet, nuotit)