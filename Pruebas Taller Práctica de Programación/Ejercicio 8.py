"""
@author: David Santiago Cardenas Rivera
"""

from array import *

arr2=[]
arrFinal=[]

def disFilas(arr2):
    arr1=[]
    while len(arr1)<9:
        for i in arr2:
            for j in i:
                if len(arr1)==9:
                    break
                arr1.append(j)
        
    return arr1

print("===OCTAVO EJERCICIO===")

figuras=[["-","-","-","-"],["o"]]

for r in range(8):
    arrFinal.append(disFilas(figuras))
    if r==3:
        arrFinal.append(disFilas(figuras[1]))

for s in arrFinal:
    for t in s:
        print(t, end=" ")
    print()