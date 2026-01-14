edades = {"alice":30, "bob":25, "charlie":35}
for nombre, edad in edades.items():
    print(f"{nombre} tiene {edad} años")

for nombre in edades.keys():
    print("nombre:", nombre)

for edad in edades.values():
    print("edad:", edad)

edades_incrementadas = {} #ejemplo de modificaicon segura de dicc
for nombre, edad in edades.items():
    edades_incrementadas[nombre] = edad + 1
print(edades_incrementadas)