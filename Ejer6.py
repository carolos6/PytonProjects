num1=float(input("Ingrese el Priemr numero: "))
num2=float(input("Ingrese el Segundo numero: "))
num3=float(input("Ingrese el Tercer numero: "))

if num1>num2 and num1>num3:
    print("El primer numero es mayor: ")
elif num2>num3 and num2>num1:
    print("El segundo numero es mayor: ")
else:
    print("El tercer numero es mayor: ")    