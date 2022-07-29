#@author: David Santiago Cardenas Rivera

import msvcrt
import numpy as np

arr1=np.full((9,9),"-")

print("===OCTAVO EJERCICIO===")


for i in range(9):
    for j in range(9):
        if i==4 or j==4:
            arr1[i][j]="o"

for i in arr1:
    for j in i:
        print(j, end="  ")
    print()

msvcrt.getch()