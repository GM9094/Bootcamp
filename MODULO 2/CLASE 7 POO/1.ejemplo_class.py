class perro:
    def __init__(self, nombre, edad): #constructor con sus atributos
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print("!Guau¡")

mi_perro = perro("Rex", 3) #objeto, instanciación de clase perro mediante objeto mi_perro
mi_perro.ladrar()

