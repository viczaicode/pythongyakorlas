def szekInit(szin:str, labszam: int):
    print(f"szín: {szin}, lábszám: {labszam}")

szekInit("kék",3)
szekInit("piros",4)
szekInit("zöld",5)

def szekStr(szin:str, labszam: int):
    return (f"szín: {szin}, lábszám: {labszam}")

print(szekStr("kék",3))
print(szekStr("piros",4))
print(szekStr("zöld",5))

