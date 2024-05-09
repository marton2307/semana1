def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # se inica en le minimo
        for j in range(i + 1, n):  # Buscamos el mínimo 
            if arr[j] < arr[min_idx]: 
                min_idx = j 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # va comparando uno por uno para q se ordene 
    return arr

entrada = [64, 34, 25, 12, 22, 11, 90]
salida_selection = selection_sort(entrada.copy())

print("Entrada:", entrada)
print("Salida Selection Sort:", salida_selection) #imprimimos el arreglo ordenado 
