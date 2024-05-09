def ingresar_arreglo(n):
    arreglo = []
    print("Ingrese los elementos del arreglo:")
    for _ in range(n):
        elemento = int(input())
        arreglo.append(elemento)
    return arreglo

def busqueda_secuencial(arreglo, numero):
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            print(f"La numero {numero} fue encontrada en la posición {i}.")
            return
    print(f"La numero {numero} no fue encontrada en el arreglo.")

def ordenar_arreglo(arreglo):
    return sorted(arreglo)

def busqueda_binaria(arreglo, numero):
    inicio = 0
    fin = len(arreglo) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if arreglo[medio] == numero:
            print(f"El numero {numero} fue encontrado en la posición {medio}.")
            return
        elif arreglo[medio] < numero:
            inicio = medio + 1
        else:
            fin = medio - 1
    print(f"El numero {numero} no fue encontrado en el arreglo.")


arreglo = [64, 34, 25, 12, 22, 11, 90, 45, 33, 28, 71, 82, 19, 17, 55, 67, 39, 59, 75, 84]
numero = 71

# Busqueda secuencial
busqueda_secuencial(arreglo, numero)

# Ordenar arreglo
arreglo_ordenado = ordenar_arreglo(arreglo)
print("Arreglo ordenado:", arreglo_ordenado)

# Busqueda binaria
busqueda_binaria(arreglo_ordenado, numero)
