from Szek import Szek

peldany1 = Szek("kék", 13)
peldany2 = Szek("piros", 4)
peldany3 = Szek("zöld", 5)
print(peldany1)
print(peldany2)
print(peldany3)

szekek = [peldany1, peldany2, peldany3]
def labakSzama():
    print("Összesen hány db székláb van a teremben?",end="")
    ossz = 0
    for index in range(0, len(szekek), 1):
        ossz += szekek[index].labszam
    print(f"{ossz} db")

labakSzama()

def maxLabszin():
    maxIndex = 0
    for index in range(1,len(szekek),1):
        if szekek[index].labszam > szekek[maxIndex].labszam:
            maxIndex = index
    print(f"A legtöbb lábbal rendelkező szék színe: {szekek[maxIndex].szin}")
maxLabszin()

def labszamok(): #megszámlálás
    print("Hány négynél több lábú szék van: ", end="")
    db = 0
    for index in range(0, len(szekek),1):
        if szekek[index].labszam > 4:
            db += 1
    print(db, "db")
labszamok()

def pirosnegylabu(): #Eldöntés
    print("Van e piros négylábú szék?", end="")
    van = False
    for index in range(0, len(szekek),1):
        if szekek[index].labszam == 4 and szekek[index].szin == "piros":
            van = True
    if van:
        print(" Igen, van.")
    else:
        print(" Nincs")
pirosnegylabu()