numero=int(input("Ingrese un numero: "))
cuenta_atras= ", ".join(map(str, range(numero, -1, -1)))
print(cuenta_atras)


numero2=int(input("Ingrese un numero: "))
cuenta_adelante=", ".join(map(str, range(1, numero2+1, +1)))
print(cuenta_adelante)