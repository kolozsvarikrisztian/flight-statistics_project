with open("vers/count-x-y-w.txt","r") as file:
    betuk = file.read()
    x = 0
    y = 0
    w = 0
    for i in betuk:
        if i == "X":
            x += 1
        elif i == "Y":
            y += 1
        elif i == "W":
            w += 1

xyw_eredm = x+y-w       