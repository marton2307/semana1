def bubble_sort(arr):
    n = len(arr)  # Obtenemos la longitud del arreglo
    for i in range(n):  # Iteramos sobre el arreglo
        swapped = False  # Inicializamos una bandera para rastrear si se han realizado intercambios
        for j in range(0, n - i - 1):  # Iteramos sobre los elementos del arreglo
            if arr[j] > arr[j + 1]:  # Comparamos el elemento actual con el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambiamos los elementos si están en el orden incorrecto
                swapped = True  # Marcamos que se ha realizado un intercambio
        if not swapped:  # Si no se realizó ningún intercambio en esta iteración
            break  # Detenemos el bucle, ya que el arreglo está ordenado
    return arr  # Devolvemos el arreglo ordenado

# Ejemplo de uso:
entrada = [64, 34, 25, 12, 22, 11, 90]
salida_bubble = bubble_sort(entrada.copy())  # Llamamos a la función bubble_sort para ordenar el arreglo

print("Entrada:", entrada)  # Imprimimos la entrada original
print("Salida Bubble Sort:", salida_bubble)  # Imprimimos la salida, es decir, el arreglo ordenado
