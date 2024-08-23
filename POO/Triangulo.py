import math  
class Triangulo:
    
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def Calcular_area(self):
        return (self.largo * self.ancho) / 2
    def Calcular_Perimetro(self):
        return math.sqrt(self.largo**2+self.ancho**2)+self.largo+self.ancho
triangulo1 = Triangulo(5 ,6)
triangulo1.Calcular_area()
triangulo1.Calcular_Perimetro()

print("Calcular calcular area:  ",triangulo1.Calcular_area())
print("Calcular perimetro del trinagulo: ",triangulo1.Calcular_Perimetro())
    
    
        
        