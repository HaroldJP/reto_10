arreglo = [1, 0, 2, 0, 3, 0, 4, 0, 5] ##Ingrese los números que desee
def mover_ceros(arreglo):
    k = 0
    for i in range(len(arreglo)):
        if arreglo[i] != 0:
            arreglo[k] = arreglo[i]
            k += 1
    for i in range(k, len(arreglo)):
        arreglo[i] = 0
    return arreglo 
print(f"Arreglo original: {arreglo}")
arreglo = mover_ceros(arreglo)
print(f"Arreglo con ceros al final: {arreglo}")