def syotetyn_kappaleen_tarkistus(kappale):
    sallitut_nuotit = ["1/4", "1/8", "1/2", "3/8", "1/16", "1", "3/16"]
    sallitut_savelet = ["C", "D", "E", "F", "G", "A", "H", "B"]
    sallitut_oktaavit = ["3", "4", "5"]

    lista = kappale.split()

    if len(lista) <= 1:
        return "Anna kappale, joka on pidempi kuin yksi nuotti/sävel"

    for alkio in lista:
        eroteltu = alkio.split("-")
        if len(eroteltu) != 2 or len(eroteltu[0]) < 2 or len(eroteltu[0]) > 3:
            return "Annettu kappale ei ollut kirjoitettu oikeassa muodossa"

        if eroteltu[0][0] not in sallitut_savelet or eroteltu[0][1] not in sallitut_oktaavit:
            return "Joku sävelistä ei ollut oikeassa muodossa"

        if eroteltu[1] not in sallitut_nuotit:
            return "Joku nuoteista ei ollu oikeassa muodossa"

        if len(eroteltu[0]) == 3:
            if eroteltu[0][2] == "#" or eroteltu[0][2] == "b":
                continue
            else:
                return "Vääränlainen ylennys- tai alennusmerkki"
    return 1
