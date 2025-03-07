# contruir un  funcionque reciba como 0parametro una lista de datos numericos y retorne la sumade dichos datos

print("--------------------------------")
print("--- SUMA DE UNA LISTA NÚMEROS ---")
print("--------------------------------")

# Definición de la función
def sumarLista(numeros):
    return sum(numeros)

# Entrada
numeros = list(map(int, input("Digite los números separados por espacio: ").split()))

# Procesamiento
resultado = sumarLista(numeros)

# Salida
print(f"\nLa suma de los números es: {resultado}")
print("\nEso era...")
