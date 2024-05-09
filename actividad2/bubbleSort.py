def bubble_sort(arr):
    n = len(arr)  # Obtenemos la longitud del arreglo
    for i in range(n):  
        swapped = False  # Inicializamos 
        for j in range(0, n - i - 1):  # repetimos el arreglo
            if arr[j] > arr[j + 1]:  # Comparamos 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambiamos los elementos si están en el orden incorrecto
                swapped = True  # Marcamos que se ha realizado un intercambio
        if not swapped:  
            break  
    return arr  # Devolvemos el arreglo ordenado


entrada = [64, 34, 25, 12, 22, 11, 90]
salida_bubble = bubble_sort(entrada.copy())  

print("Entrada:", entrada)  # Imprimimos el array 
print("Salida Bubble Sort:", salida_bubble)  # Imprimimos el array listo 
