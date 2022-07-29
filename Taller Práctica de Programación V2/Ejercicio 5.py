"""
@author: David Santiago Cardenas Rivera
"""

from random import randint
import msvcrt

i=0
random=0
numeros=[]
sortedNumeros=[]
j=0
temporal=0


print("===QUINTO EJERCICIO===")
while len(numeros)<20:
    random=randint(15,86)
    numeros.append(random)

sortedNumeros=numeros.copy()
sortedNumeros.sort()
for i in range(0,len(sortedNumeros)):
    for j in range(i+1, len(sortedNumeros)):
        if(sortedNumeros[i]<sortedNumeros[j]):
            temporal=sortedNumeros[i]
            sortedNumeros[i]=sortedNumeros[j]
            sortedNumeros[j]=temporal

print("El vector antes del ordenamiento:")
print(f"{numeros}\n")
print("El vector despues del ordenamiento:")
print(f"{sortedNumeros}")

msvcrt.getch()