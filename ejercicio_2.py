# contruir una funcio que reciba una cadena digitada(como paramero) por el usuario y que lo muestre n veces en la pantalla. el valor de n tambies digitado por el usuario

print("------------------------------")
print("--- MOSTRAR CADENA N VECES ---")
print("------------------------------")

# Definición de la función
def mostrarCadena(texto, n):
    for i in range(1, n + 1):
        print(f"{i}. {texto}")

# Entrada
texto = input("Digite una cadena: ")
n = int(input("Digite cuántas veces desea mostrarla: "))

# Procesamiento
mostrarCadena(texto, n)

# Salida
print("\nEso era...")
