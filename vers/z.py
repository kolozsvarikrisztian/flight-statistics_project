with open("vers/after-z.txt","r") as file:
    szamok = "0123456789"
    db = 0
    z = 0
    for sor in file:
        for index,kar in enumerate(sor):
            if kar == "Z" and sor[index+1] in szamok:
                z += int(sor[index+1])
                db += 1

atlag = z / db
          
print(round(atlag))
                
    