from fibonacci import fib_megold
from z import z_atlag
from xyw import xyw_eredm

eltolas_ertek = fib_megold + z_atlag + xyw_eredm


abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nabc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

cabc = []
cnabc = []

for index,elem in enumerate(abc):
    if index+eltolas_ertek < len(abc):
        cabc.append(abc[index+eltolas_ertek])
    elif index+eltolas_ertek >= len(abc):
        elt = (index+eltolas_ertek) - len(abc)
        cabc.append(abc[elt])
        
for index,elem in enumerate(abc):
    if index+eltolas_ertek < len(abc):
        cnabc.append(abc[index+eltolas_ertek].upper())
    elif index+eltolas_ertek >= len(abc):
        elt = (index+eltolas_ertek) - len(abc)
        cnabc.append(abc[elt].upper())

with open("vers/caesar.txt","r",encoding="utf-8") as file:
    k_vers = list(file.read())
    vers= []
    for index,elem in enumerate(k_vers):
        if elem.lower() not in abc:
            vers.append(elem)
        elif elem in abc:
            eltolt = cabc.index(elem) 
            vers.append(abc[eltolt])
        elif elem in nabc:
            eltolt = cnabc.index(elem) 
            vers.append(nabc[eltolt])
        
vers_szoveg = ''.join(vers)

with open("vers/vers_szoveg.txt","w",encoding="utf-8") as iro:
    iro.write(vers_szoveg)