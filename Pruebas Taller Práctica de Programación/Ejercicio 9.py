"""
@author: David Santiago Cardenas Rivera
"""

from random import randint

arrEn=[]
tam=0
arrRan=[]

def verificarValor(val,arr):

    if arr.count(val)>0:
        print(f"El valor {val} está en el arreglo")

    elif arr.count(val)==0:
        print(f"El valor {val} no está en el arreglo")

def generarRandom(tam1):

    for i in range(tam1):
        random=randint(1,50)
        arrRan.append(random)
    
    return arrRan

print("===NOVENO EJERCICIO===")

gen=str(input("Para probar funcionamiento, ¿desea generar un arreglo al azar?\nEscriba Y para sí o N para no: ").capitalize())

if gen=="Y":
    tam=int(input("Digite el tamaño del arreglo: "))
    arr1=generarRandom(tam)
    valor=int(input("Digita el valor a buscar en el arreglo: "))
    print(arr1)
    verificarValor(valor,arr1)

elif gen=="N":
    arrEn=[int(v) for v in input("Escribe el arreglo a identificar con valores separados por coma: ").split(",")]      #El arreglo se escribe de la siguiente manera. Ej: 23,45,67,89,12,34
    print("="*90)
    valor=int(input("Digita el valor a buscar en el arreglo: "))
    print(arrEn)
    verificarValor(valor,arrEn)

