"""
@author: David Santiago Cardenas Rivera
"""
import msvcrt

numMayor=0
cantidadm=0
cantidad=0
entrada=0
numeros=[]
i=0

print("===SEGUNDO EJERCICIO===")
cantidad=int(input("Digita la cantidad de numeros a ingresar: "))

for i in range(cantidad):
    entrada=int(input(f"Ingrese el numero {i+1}: "))
    numeros.append(entrada)

numeros.sort()
numMayor=numeros[cantidad-1]
cantidadm=numeros.count(numMayor)

print(f"\nEl mayor numero leido fue: {numMayor}\nLa cantidad de veces que fue ingresado fue: {cantidadm}")

msvcrt.getch()