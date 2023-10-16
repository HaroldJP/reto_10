##Aquí el usuario digita manualmente el arreglo con la longitud que desee
lista = [1, 1, 1] ##Esta es la lista, que puede ser de la longitud que desee
def promedio(lista):
    d = 0
    for i in range(len(lista)):
        d += lista[i]
    return d / len(lista)
if __name__ == "__main__":
    resultado = promedio(lista)
    print(f"El promedio entre el arreglo de reales comprendido por el arreglo de números ingresado es {resultado}")