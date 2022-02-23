fibonacci = [0,1]
index = 2
while index != 50:
    fib_szam = fibonacci[index-1] + fibonacci[index-2]
    fibonacci.append(fib_szam)
    index += 1
    
otven = str(fibonacci[49])
megoldas = int(otven[0]) - int(otven[len(otven)-1])

print(megoldas)