#@author: David Santiago Cardenas Rivera

from prettytable import PrettyTable
import msvcrt

bultos=[]
pesoTot=0
pesoBulto=0
valor=0
ingresos=0
promedio=0
todo=[]
todo2=[]
i=0
a=0
b=0

def calcValor(pes):
    if pes>=0 and pes<=25:
        return 0
    if pes>=26 and pes<=300:
        a=pes*1500
        return a
    if pes>=301 and pes<=500:
        b=pes*2500
        return b 

def contenidoTabla(tab):
    tabla=PrettyTable()
    labels=["BULTO", "PESO", "PRECIO COP", "PRECIO USD"]
    tabla.field_names=labels
    for item in tab:
        tabla.add_row(item)
    print(tabla)

print("===DECIMO EJERCICIO===\n")

cantBultos=int(input("Digite la cantidad de bultos a ingresar: "))
for i in range(cantBultos):
    pesoBulto=int(input(f"Digite el peso de bulto número {i+1}: "))

    pesoTot=pesoTot+pesoBulto

    while not(pesoTot<=18000 and pesoBulto<=500):  
        print("El valor ingresado excede la capacidad máxima")
        pesoTot=pesoTot-pesoBulto
        pesoBulto=int(input(f"Digite el peso de bulto número {i+1}: "))
        pesoTot=pesoTot+pesoBulto
    
    valor=calcValor(pesoBulto)
    valorDol=round(valor/4453.34,2)
    ingresos=ingresos+valor
    bultos.append(pesoBulto)
    todo2.append(i+1)
    todo2.append(f"{pesoBulto} kg")
    todo2.append(f"${valor:,.0f}")
    todo2.append(f"${valorDol:,.2f}")
    todo.append(todo2)
    todo2=[]
        
bultos.sort()
pesoMax=bultos[cantBultos-1]
pesoMin=bultos[0]
promedio=pesoTot/cantBultos
ingresosDol=round(ingresos/4453.34,2)

print("\n===TABLA===")
contenidoTabla(todo)
print("\n"+"="*90)
print(f"El numero total de bultos ingresados para el vuelo es {cantBultos} con una carga total de {pesoTot} kg.")
print(f"El peso del bulto más pesado es {pesoMax} kg.\nEl peso del bulto más liviano es {pesoMin} kg.")
print(f"El peso promedio de los bultos es de {promedio:.2f} kg.")
print(f"El ingreso en |COP| es de ${ingresos:,.0f} y en |USD| de ${ingresosDol} por concepto de carga.")

msvcrt.getch()