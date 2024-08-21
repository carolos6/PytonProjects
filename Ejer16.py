

def Conversion(GradosCelsius):
        fa=(GradosCelsius*9)/5+32
        return fa
    
temperatura_Celsius=float(input("Ingrese la temperatura en Celsius"))

respuesta=Conversion(temperatura_Celsius)
print("La conversion fue", respuesta)
