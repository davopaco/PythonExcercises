"""
@author: David Santiago Cardenas Rivera
"""

from random import randint
import msvcrt

A=[]
B=[]
ATemp=[]
BTemp=[]
i=0
j=0

print("===SEXTO EJERCICIO===")
while len(A)<10:
    random=randint(200,1000)
    A.append(random)

while len(B)<10:
    random=randint(200,1000)
    B.append(random)

print(f"El vector A es:\n{A}\n")
print(f"El vector B es:\n{B}\n")

for i in range(len(A)):
    if A[i]%2!=0:
        ATemp.append(A[i])


for j in range(len(B)):
    if B[j]%2==0:
        BTemp.append(B[j])

A.clear()
B.clear()
A.extend(BTemp)
B.extend(ATemp)

print(f"El nuevo vector A es:\n{A}\n")
print(f"El nuevo vector B es:\n{B}\n")

msvcrt.getch()