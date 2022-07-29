"""
@author: David Santiago Cardenas Rivera
"""

from random import randint
import msvcrt

i=0
random=0
numeros=[]
acum=0
numMenor=0
numMayor=0
promedio=0
j=0
res=""
cantidad=0

print("===CUARTO EJERCICIO===")
cantidad=int(input("Digita la cantidad de numeros al azar: "))

for i in range(cantidad):
    random=randint(1,100)
    numeros.append(random)
    acum+=random
    if res=="":
        res=str(random)
    else:
        res+=', '+str(random)

numeros.sort()
numMayor=numeros[cantidad-1]
numMenor=numeros[0]
promedio=(numMayor+numMenor)/2

print("\nLos valores son:")
print(res)
print(f"\nEl mayor numero generado es: {numMayor}\nEl menor numero generado es: {numMenor}\nEl promedio del menor y el mayor numero es: {promedio:,.2f}")

msvcrt.getch()