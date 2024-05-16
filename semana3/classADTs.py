class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.head = None

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.head
        self.head = nuevo_nodo

    def eliminar(self, dato):
        current = self.head
        if current.dato == dato:
            self.head = current.siguiente
            return
        while current.siguiente:
            if current.siguiente.dato == dato:
                current.siguiente = current.siguiente.siguiente
                return
            current = current.siguiente

    def obtener(self, indice):
        current = self.head
        count = 0
        while current:
            if count == indice:
                return current.dato
            count += 1
            current = current.siguiente
        return None

def main():
    lista = ListaEnlazada()
 
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    print("Lista completa:")
    current = lista.head
    while current:
        print(current.dato)
        current = current.siguiente

    lista.eliminar(20)
    print("Lista después de eliminar 20:")
    current = lista.head
    while current:
        print(current.dato)
        current = current.siguiente

    elemento = lista.obtener(1)
    print("Elemento en el índice 1:", elemento)

if __name__ == "__main__":
    main()
