##Aquí el usuario ingresa los arreglos que desee
lista1 = [1, 1, 1]##Ingrese los números que desee
lista2 = [1, 1, 1]##Ingrese los números que desee, pero que tenga la misma cantidad de números que la primera lista.
def producto_punto(lista1, lista2):
    producto = 0
    if len(lista1) != len(lista2):
        print("Pero le di la indicación que los arreglos tenían que ser de la misma longitud. Avíspese.")
    else:
        for i in range(len(lista1)):
            producto += lista1[i] * lista2[i]
        return producto
if __name__ == "__main__":
    punto = producto_punto(lista1, lista2)
    print(f"El producto punto entre los arreglos de números ingresados es {punto}")