"""
@author: David Santiago Cardenas Rivera
"""

from random import randint
import msvcrt

tam=0
arrRan=[]

def verificarValor(val,arr):
    if arr.count(val)==1:
        print(f"El valor {val} está en el arreglo {arr.count(val)} vez.")
    
    elif arr.count(val)>1:
        print(f"El valor {val} está en el arreglo {arr.count(val)} veces.")

    elif arr.count(val)==0:
        print(f"El valor {val} no está en el arreglo")

def generarRandom(tam1):

    for i in range(tam1):
        random=randint(1,50)
        arrRan.append(random)
    
    return arrRan

print("===NOVENO EJERCICIO===")

tam=int(input("Digite el tamaño del arreglo: "))
arr1=generarRandom(tam)
print("\nLos valores del arreglo son:")
print(arr1)
valor=int(input("\nDigita el valor a buscar en el arreglo (1 a 50): "))
verificarValor(valor,arr1)

msvcrt.getch()

