"""
@author: David Santiago Cardenas Rivera
"""

from random import randint


vector=[]
vectorantes=[]
temporal=0
k=0
j=19

print("===SEPTIMO EJERCICIO===")

while len(vector)<20:
    random=randint(0,10)
    vector.append(random)

vectorantes=vector.copy()

for i in range(0,len(vector)):
    if vector[i]==0:
        temporal=vector[i]
        k=i
        for k in range(k,len(vector),1):
            if k<=18:
                vector[k]=vector[k+1]

if vectorantes.count(0)>0:
    for r in reversed(range(len(vectorantes)-vectorantes.count(0),len(vectorantes))):
        vector[r]=temporal        

print(f"El vector antes es:\n {vectorantes}")
print(f"El vector despues es:\n {vector}")
