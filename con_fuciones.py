print("----------------------------")
print("-BUSCAR UN NUMEROEN CONJUTO-")
print("----------------------------")

#Difinicion de la funcion 
def buscarDatoEnLista(datoABuscar,lidts):
    r =False
    for  i in lista:
        if i  == datoABuscar:
            r = True 
    return r

#Entrada 
dato ==int(input("numero a buscar")) #se describe el dato del usuario

#procesamiento
lista == [1,2,3,4,5] #se almacena unalista de datos
if buscarDatosEnLista(dato, lista):
    print("lo encontre")
else
    print("no lo encontre")
    