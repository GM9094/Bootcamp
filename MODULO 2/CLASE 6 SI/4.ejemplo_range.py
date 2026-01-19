for i in range(5):
    print("numero", i)

for i in range(2, 6):
    print("numero", i)

for i in range(1, 10, 2):
    print("numero", i)

numeros = [10, 20, 30, 40, 50]
for i in range(len(numeros)): #genera una secuencia de indices basada en la longitud de la lista numeros
    numeros[i] += 5
print(numeros)