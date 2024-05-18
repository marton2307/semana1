def find_max(arr):
    if not arr:
        return None  # Manejo de arreglo vacío
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
    return max_element

def find_min(arr):

    ##Encuentra el elemento menor en un arreglo.
   
    if not arr:
        return None  # Manejo de arreglo vacío
    min_element = arr[0]
    for num in arr:
        if num < min_element:
            min_element = num
    return min_element

def bubble_sort(arr):

   ## Ordena un arreglo utilizando el algoritmo Bubble Sort.

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambio de elementos
    return arr

# Pruebas y validación
test_arrays = [
    [34, 7, 23, 32, 5, 62],
    [12, 11, 13, 5, 6],
    [5, 5, 5, 5, 5],
    [],
    [1]
]

# Pruebas para encontrar el elemento mayor y menor
for arr in test_arrays:
    if arr:
        print(f"Array: {arr}")
        print(f"Max: {find_max(arr)}")
        print(f"Min: {find_min(arr)}")
    else:
        print("Array vacío.")

# Pruebas para el algoritmo de ordenación Bubble Sort
for arr in test_arrays:
    if arr:
        print(f"Original array: {arr}")
        print(f"Bubble sorted: {bubble_sort(arr[:])}")  # Usar copia del arreglo
    else:
        print("Array vacío.")
