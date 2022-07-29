"""
@author: David Santiago Cardenas Rivera
"""

import math
import msvcrt

numPrimos=[]
i=0
num=2
fact=0
j=0
res=""
cantidad=0

print("===TERCER EJERCICIO===")
cantidad=int(input("Digita la cantidad de numeros primos que solicita: "))

while i<cantidad:
    fact=math.factorial(num-1)
    if fact % num == num-1:
        numPrimos.append(num)
        i=i+1
    num=num+1


for j in range(len(numPrimos)):
    if res=="":
        res=str(numPrimos[j])
    else:
        res=res+', '+str(numPrimos[j])

print(f"\nLos primeros {cantidad} numeros primos son:")
print(res)

msvcrt.getch()