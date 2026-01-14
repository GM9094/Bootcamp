class empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    def mostrar_info(self):
        return f"nombre: {self.nombre}, salario: {self.salario}"
    def obtener_abono(self, nuevo_monto):
        return  self.salario + self.salario*0.1

class gerente(empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)