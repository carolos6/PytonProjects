def palindromo(cadena):
    cadena = cadena.replace("","").lower()
    return cadena == cadena[::-1]

cadena=input("Ingresar cadena: ")
if palindromo(cadena):
    print("La cadena es palindromo")
else:
    print("La cadena no es palindromo")