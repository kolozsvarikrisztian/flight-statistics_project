with open("vers/after-z.txt","r") as file:
    szamok = "0123456789"
    lista = file.read()
    z = []
    for index,elem in enumerate(lista):
        if elem == "Z":
            keres = 1
            szam = 0
            while lista[index+keres] in szamok:
                szam += int(lista[index+keres])
                keres+=1
            if szam != 0:
                z.append(szam)
    
z_atlag = round(sum(z) / len(z))    