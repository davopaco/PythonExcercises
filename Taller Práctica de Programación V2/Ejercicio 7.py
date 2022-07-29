"""
@author: David Santiago Cardenas Rivera
"""

import msvcrt
from random import randint

vector=[]
vectorantes=[]
temporal=0
con=0

print("===SEPTIMO EJERCICIO===")

while len(vector)<20:
    random=randint(0,10)
    vector.append(random)

vectorantes=vector.copy()

while(con<vector.count(temporal)):
    for i in range(len(vector)):
        if vector[i]==0:
            temporal=vector.pop(i)
            vector.append(temporal)
    con=con+1

print(f"El vector antes es:\n {vectorantes}\n")
print(f"El vector despues del ordenamiento es:\n {vector}")

msvcrt.getch()