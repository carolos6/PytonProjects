
Cantidad=float(input("Ingrese la cantidad a invertir: "))
InteresAnual=float(input("Ingrese el interes Anual: "))
Año=int(input("Ingrese el numero de años: "))
for Año in range(1, Año+1):
    Cantidad+=Cantidad*InteresAnual
    print("El año: ", Año," la cantida fue: ",Cantidad)
    