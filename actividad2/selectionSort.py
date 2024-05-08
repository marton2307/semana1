def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # Inicializamos el índice del mínimo como el índice actual
        for j in range(i + 1, n):  # Buscamos el mínimo en el subarreglo no ordenado
            if arr[j] < arr[min_idx]:  # Si encontramos un elemento menor que el mínimo actual
                min_idx = j  # Actualizamos el índice del mínimo
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambiamos el mínimo con el primer elemento del subarreglo no ordenado
    return arr

# Ejemplo de uso:
entrada = [64, 34, 25, 12, 22, 11, 90]
salida_selection = selection_sort(entrada.copy())

print("Entrada:", entrada)
print("Salida Selection Sort:", salida_selection)
