#Algoritmo numeros primos


primoslista=[]
i=2
N=int(input("Ingrese la cantidad de numeros primos a imprimir: "))

def primos(n):
    for i in range(2,n):
        if (n%i)==0:
            return False
    return True

try:
    while True:
        if primos(i):
            primoslista.append(i)
            if(len(primoslista)==N):
                break
        i+=1
    print(f"Los primeros {N} numeros primos son: {str(primoslista)[1:-1]}")

except:
    print("Usted puso un valor no permitido.")