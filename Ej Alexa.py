import msvcrt
import numpy as np

print("*"*10 + " Octavo ejercicio "+"*"*10) 
figuras=np.full((9,9),"-")
figuras[4]="o"
figuras[:,4]="o" 
for d in range (9): 
    for f in range (9): 
        print(figuras[d][f], end='  ') 
    print() 

msvcrt.getch()