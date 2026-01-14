class empleado:
    def __init__(self, nombre, rol, salario):
        self.nombre = nombre
        self.rol = rol
        self.salario = salario
    def mostrar_info(self):
        print(f"nombre : {self.nombre}, rol : {self.rol}, salario : {int(self.salario)}")
    def actualizar_salario(self, nuevo_monto):
        self.salario = nuevo_monto 
    def gana_mas_que(self, promedio):
        return self.salario > promedio

c1 = empleado("Ana", "Analisador", 1200)
c2 = empleado("jorge", "desarrollador", 3000)
c3 = empleado("jorge", "Jefe de Proyecto", 5000)

empleados = [c1, c2, c3]
total_salario = 0
for i in empleados:
     i.mostrar_info()
     total_salario += i.salario

promedio = total_salario/3
print(promedio)

for i in empleados:
    if i.gana_mas_que(promedio):
        print(True)



