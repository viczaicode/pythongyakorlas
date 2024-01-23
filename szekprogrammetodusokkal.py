from Szek import Szek
def peldanyoklistaban():
    peldany1 = Szek("kék", 13)
    peldany2 = Szek("piros", 4)
    peldany3 = Szek("zöld", 5)
    szekek = [peldany1, peldany2, peldany3]
    return szekek

szekek = peldanyoklistaban()
def listakiir(lista):
    for index in range(0, len(szekek),1):
        print(lista[index])
#rövid verzio:
#listakiir(peldanyoklistaban())
#hosszu verzio:
szeklista = peldanyoklistaban()
listakiir(szeklista)

def osszegzes(szekek):
    print("Összesen hány db székláb van a teremben?",end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")

osszegzes(szeklista)

def maximumkivalasztas(szekek):
    maxIndex = 0
    for index in range(1,len(szekek),1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")

maximumkivalasztas(szeklista)

def megszamolas(szekek): #megszámlálás
    print("Hány négynél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek),1):
        if szekek[index].labszam > 4:
            db += 1
    print(db, "db")
megszamolas(szeklista)

def eldontes(szekek): #Eldöntés
    print("Van e piros négylábú szék?", end="")
    van = False
    for index in range(0, len(szekek),1):
        if szekek[index].labszam == 4 and szekek[index].szin == "piros":
            van = True
    if van:
        print(" Igen, van.")
    else:
        print(" Nincs")
eldontes(szeklista)
