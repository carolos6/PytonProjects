def calcular_suma(lista_num):
    Suma=0
    for i in  lista_num:
        Suma+=i
    return Suma
        
Lista=[1,2,3,4,5,6]

suma_numeros= calcular_suma(Lista)
print("La suma de los numeros es: ",suma_numeros)
    