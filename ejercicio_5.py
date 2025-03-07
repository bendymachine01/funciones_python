# construir una funcion que reciba como prametro un lista de datosnumericos y retorne el promedio de los datos pares 

print("----------------------------------")
print("--- PROMEDIO DE NÚMEROS PARES ---")
print("----------------------------------")

# Definición de la función
def promedioPares(numeros):
    pares = [num for num in numeros if num % 2 == 0]
    return sum(pares) / len(pares) if pares else 0

# Entrada
numeros = list(map(int, input("Digite los números separados por espacio: ").split()))

# Procesamiento
resultado = promedioPares(numeros)

# Salida
print(f"\nEl promedio de los números pares es: {resultado:.2f}")
print("\nEso era...")
