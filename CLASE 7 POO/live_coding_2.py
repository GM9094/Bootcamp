class empleado:
    def __init__(self, nombre, rol, salario):
        self.nombre = nombre
        self.rol = rol
        self.salario = salario
    def mostrar_info(self):
        return f"empleado : {self.nombre}, rol : {self.rol}, salario : {self.salario}"
    

e1 = empleado("ana", "analista", 1300)
print(e1.mostrar_info())

class gerente(empleado):
    def __init__(self, nombre, salario, equipo_size):
        super().__init__(nombre, "gerente", salario)
        self.equipo_size = equipo_size

    def mostrar_info(self):
        return f"gerente: {self.nombre}, equipo: {self.equipo_size}, salario :{self.salario}"

g = gerente("juan", 200000)
print(g.mostrar_info())        
