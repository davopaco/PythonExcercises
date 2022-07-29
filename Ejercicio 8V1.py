"""
@author: David Santiago Cardenas Rivera
"""
from array import *
import msvcrt

arr1=[]
arr2=[]

for v in range(9):                                                                       
    for w in range(9):
        arr2.append("")
    arr1.append(arr2)
    arr2=[]

print("===OCTAVO EJERCICIO===")

figuras=["-","o"]

for i in range(9):
    for j in range(9):
        if i==4 or j==4:
            arr1[i][j]=figuras[1]
        else:
            arr1[i][j]=figuras[0]

for s in arr1:
    print(s)

msvcrt.getch()