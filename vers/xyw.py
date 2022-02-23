with open("count-x-y-w.txt","r") as file:
    lista = []
    x = 0
    y = 0
    w = 0
    for i in file:
        lista = file.read()
    for i in lista:
        if i == "X":
            x += 1
        elif i == "Y":
            y += 1
        elif i == "W":
            w += 1

eredmeny = x+y-w            
print(eredmeny)