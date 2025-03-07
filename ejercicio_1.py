# construir una funcionque reciba su nombre como parametro y que lo muestre 5 vece en la pantalla

print("-----------------------------------")
print("--- MOSTRAR NOMBRE EN PANTALLA ----")
print("-----------------------------------")

# Definición de la función
def mostrarNombre(nombre):
    for i in range(1, 6):
        print(f"{i}. {nombre}")

# Entrada
nombre = input("Digite su nombre: ")

# Procesamiento
mostrarNombre(nombre)

# Salida
print("\nEso era...")