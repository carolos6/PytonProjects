class persona:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        

persona1 = persona.mostrar_detalle("Leo", 20)
persona1.mostrar_detalle()  