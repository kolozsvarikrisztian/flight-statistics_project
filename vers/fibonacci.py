fibonacci = [1,2]
index = 2

while index != 50:
    fib_szam = fibonacci[index-1] + fibonacci[index-2]
    fibonacci.append(fib_szam)
    index += 1
    
otven = str(fibonacci[49])
fib_megold =  int(otven[len(otven)-1]) - int(otven[0])