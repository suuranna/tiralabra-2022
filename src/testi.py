from trierakenne import TrieRakenne
from json_funktiot import *
import random

def rekursio(numero, lista, max):
    lista.append(numero)
    print(lista)
    if len(lista) == max and lista[len(lista) - 1] == 8:
        return lista
    if len(lista) == max:
        print("liian pitkä")
        lista.pop()
        return
    
    #print("numero on")
    #print(numero)

    for i in range(0, 10):
        luku = random.randint(1, 10)
        #lista.append(luku)
        #print("luku on")
        #print(luku)
        r = rekursio(luku, lista, max)
        if isinstance(r, list):
            return r

def main():
    data = avaaJson()
    print(len(data["savelet"]))
    print(len(data["nuotit"]))
    kappale = "A4-1/8 G4-1/8 A4-1/8 G4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A3-3/8 G3-3/8 A4-1/8 G4-1/8 A4-1/8 G4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A3-3/8 G3-3/8 G4-1/8 E4-1/8 G4-1/8 E4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A3-3/8 G3-3/8 G4-1/8 E4-1/8 G4-1/8 E4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A4-3/8 B4-3/8 A4-1/8 G4-1/8 A4-1/8 G4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A3-3/8 G3-3/8 A4-1/8 G4-1/8 A4-1/8 G4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A3-3/8 G3-3/8 G4-1/8 E4-1/8 G4-1/8 E4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A3-3/8 G3-3/8 G4-1/8 E4-1/8 G4-1/8 E4-1/8 D4-1/8 E4-1/8 D4-1/8 C4-1/8 A3-1/8 G3-1/8 A4-3/8 B4-3/8"
    lista = kappale.split()
    print(len(lista))
    trie = TrieRakenne("sävelet")
    trie2 = TrieRakenne("nuotit")

    trie.alusta()
    trie2.alusta()



    pisin = trie2.pisin
    print(pisin)    
    for i in range(1, pisin + 1):
        print(i)
        kappale = trie2.luo_kappale(i, i)
        print(len(kappale))
    #kappale = trie2.luo_kappale(6, 6)

    print("---------")
    #print(rekursio(0, [], 10))

if __name__ == '__main__':
    main()