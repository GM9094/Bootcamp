class perro:
    def __init__(self, nombre, edad): #constructor con sus atributos
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_info(self):
        #interporlación
        return f"nombre: {self.nombre}, edad: {self.edad} años"

mi_perro = perro("Firulais", 2)
print(mi_perro.mostrar_info())