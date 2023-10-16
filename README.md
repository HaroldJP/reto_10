# reto_10

### Punto 1

Desarrollar un algoritmo que calcule el promedio de un arreglo de reales.

Aquí me inspiré y dejé dos opciones. Ambos programan sirven para lo mismo con la diferencia que el primero que voy a colocar sirve para calcular el promedio de un areglo de 3 números ingresados por teclado.

```python
##Vamos a utilizar un arreglo de 3 números
a = float(input("Escriba un número real: "))
b = float(input("Escriba otro número real: "))
c = float(input("Escriba un último número real: "))
lista = [a, b, c]
def promedio(a, b, c) -> float:
    d = 0
    for i in range(len(lista)):
        d += lista[i]
    return d / len(lista)
if __name__ == "__main__":
    resultado = promedio(a, b, c)
    print(f"El promedio entre el arreglo de reales comprendido por los números {a}, {b}, y {c} es {resultado}")
```

Ahora, como mencioné anteriormente, este programa sirve para lo mismo pero ahora el usuario ingresa de forma manual dentro del código los números que quiera con la longitud que quiera en el arreglo.

```python
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
```

### Punto 2

Desarrollar un algoritmo que calcule el producto punto de dos arreglos de números enteros (reales) de igual tamaño.

Aquí hice exactamente lo mismo que con el punto anterior. Primero va el programa que sirve para ingresar por teclado dos arreglos de 3 números cada uno, y después uno en el que el usuario puede ingresar dentro del código los números que quiera con la longitud que quiera.

Para ingresar por teclado:

```python
##Vamos a utilizar arreglos de 3 números
a = float(input("Ingrese el primer número del primer arreglo: "))
b = float(input("Ingrese el segundo número del primer arreglo: "))
c = float(input("Ingrese el tercer número del primer arreglo: "))
d = float(input("Ingrese el primer número del segundo arreglo: "))
e = float(input("Ingrese el segundo número del segundo arreglo: "))
f = float(input("Ingrese el tercer número del segundo arreglo: "))
lista1 = [a, b, c]
lista2 = [d, e, f]
def producto_punto(lista1, lista2):
    producto = 0
    for i in range(len(lista1)):
        producto += lista1[i] * lista2[i]
    return producto
if __name__ == "__main__":
    punto = producto_punto(lista1, lista2)
    print(f"El producto punto entre los arreglos de números [{a}, {b}, {c}] y [{d}, {e}, {f}] es {punto}")
```

Para ingresar dentro del código con cualquier longitud:

```python
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
```

### Punto 3

Hacer un algoritmo que deje al final de un arreglo de números todos los ceros que aparezcan en dicho arreglo.

```python
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
```
