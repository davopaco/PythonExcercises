"""
@author: David Santiago Cardenas Rivera
"""
import msvcrt

sumtot=0
sumpos=0
sumneg=0
numero=0
cantidad=0

print("===PRIMER EJERCICIO===")
cantidad=int(input("Digita la cantidad de numeros a ingresar: "))

for i in range(cantidad):
    numero=int(input(f"Ingresa el número {i+1}: "))
    sumtot=sumtot+numero

    if numero>=0:
        sumpos=sumpos+numero
    else:
        sumneg=sumneg+numero

print(f"\n-----SUMAS-----\nLa suma total es de: {sumtot}\nLa suma de positivos es de: {sumpos}\nLa suma de negativos es de: {sumneg}")

msvcrt.getch()