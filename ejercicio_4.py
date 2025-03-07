# construir una funcion  que reciba como parametro una listade dato numericos y que retorne el promedio de dchos datos

print("-----------------------------------")
print("--- PROMEDIO DE UNA LISTA NÚMEROS ---")
print("-----------------------------------")

# Definición de la función
def promedioLista(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

# Entrada
numeros = list(map(int, input("Digite los números separados por espacio: ").split()))

# Procesamiento
resultado = promedioLista(numeros)

# Salida
print(f"\nEl promedio de los números es: {resultado:.2f}")
print("\nEso era...")
