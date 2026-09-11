import math

num=1
primo= [2,3]

for num in range (4, 250):

    es_primo= True  

    for divisor in range(2, int(math.sqrt(num)) + 1):
    
        if num % divisor == 0:
            es_primo = False
            break

    if es_primo:
        primo.append(num)

with open("primos.txt", "w") as archivo:
    archivo.write(str(primo))