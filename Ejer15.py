import math
def calcular_area(r):
    area= math.pi*r**2
    return area



radio=float(input("Introduce el area del circulo"))
area=calcular_area(radio)
print("El area es : ", area)