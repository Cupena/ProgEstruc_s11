def crear_nodo(dato):
    return {
        "dato": dato,
        "izquierdo": None,
        "derecho": None
    }


raiz = crear_nodo("A")
raiz["izquierdo"] = crear_nodo("B")
raiz["derecho"] = crear_nodo("C")


def recorrer(nodo):
    if nodo is not None:
        print(nodo["dato"])
        recorrer(nodo["izquierdo"])
        recorrer(nodo["derecho"])


print("Recorrido del árbol:")
recorrer(raiz)