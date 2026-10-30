
def __init__(self, dato):
    self.dato = dato
    self.izquierdo = None
    self.derecho = None
    raiz = Nodo("Ana")
        
    raiz.izquierdo = Nodo("Luis")
    raiz.derecho = Nodo("María")
    print("Raíz:", raiz.dato)
    print("Hijo izquierdo:", raiz.izquierdo.dato)
    print("Hijo derecho:", raiz.derecho.dato)


def __init__(self, dato):
    self.dato = dato
    self.izquierdo = None
    self.derecho = None
    raiz = Nodo("A")
    raiz.izquierdo = Nodo("B")
    raiz.derecho = Nodo("C")