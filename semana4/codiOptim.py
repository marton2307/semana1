import random
import time

# Genera una lista de números aleatorios
def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

# Encuentra el elemento máximo y suma todos los elementos en la lista
def maximo_y_suma(lista):
    maximo = lista[0]
    suma = 0
    for num in lista:
        if num > maximo:
            maximo = num
            suma += num
    return maximo, suma

if __name__ == "__main__":
    tamano_lista = 1000
    lista = generar_lista(tamano_lista)

    start_time = time.time()
    maximo, suma = maximo_y_suma(lista)
    end_time = time.time()
    optimized_time = end_time - start_time

    print(f"Lista: {lista}")
    print(f"Máximo: {maximo}")
    print(f"Suma: {suma}")
    print(f"Tiempo optimizado: {optimized_time:.10f} segundos")
