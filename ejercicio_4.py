# construir una funcion  que reciba como parametro una lista de datos numericos y que retorne el promedio de dchos datos

import random

print("------------------------------")
print("------ LISTA DE DATOS --------")
print("------------------------------")

# Definición de la función
def calcular_suma_lista(lista):
    return sum(lista)

# Entrada
lista = []
n = int(input("Ingrese el tamaño de la lista: "))

for i in range(n):
    num = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    lista.append(num)
    print(f"Número {i+1}: {num}")

# Procesamiento
suma = calcular_suma_lista(lista)

# Salida
print("La suma de la lista es: ", suma)
