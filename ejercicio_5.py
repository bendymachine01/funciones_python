# construir una funcion que reciba como prametro un lista de datos numericos y retorne el promedio de los datos pares 

import random

print("------------------------------")
print("------ LISTA DE DATOS --------")
print("------------------------------")

# Definición de la función
def calcular_promedio_pares(lista):
    pares = [num for num in lista if num % 2 == 0]
    if pares:
        return sum(pares) / len(pares)
    else:
        return 0

# Entrada
lista = []
n = int(input("Ingrese el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    lista.append(num)
    print(f"Número {i+1}: {num}")

# Procesamiento
promedio_pares = calcular_promedio_pares(lista)

# Salida
print("El promedio de los números pares en la lista es: ", promedio_pares)

