class empleado:
    def __init__(self, nombre, rol, salario):
        self.nombre = nombre
        self.rol = rol
        self.salario = salario
    
    def mostrar_info(self):
        print(f"nombre : {self.nombre}, rol : {self.rol}, salario : {self.salario}")

    def actualizar_salario(self, nuevo_monto):
        self.salario = nuevo_monto

    def __str__(self):
        return f"nombre empleado : {self.nombre}, su rol :{self.rol}, salario : {self.salario}"     

c1 = empleado("Ana", "Analisador", 1200)
c2 = empleado("jorge", "desarrollador", 3000)
c1.mostrar_info()
c2.mostrar_info()
c1.actualizar_salario(1500)
c1.mostrar_info()

print(c1)

empleados = [c1, c2]
