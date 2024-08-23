import math 
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def CalcularArea(self):
        return math.pi * (self.radio ** 2)
    
    def Calcular_circunferencia(self):
        return 2*math.pi * (self.radio)
    
    
    
circulo1= Circulo (5)
print ("El area seria: ", circulo1.CalcularArea())
print ("La circunferencia vendria ser: ", circulo1.Calcular_circunferencia())
    