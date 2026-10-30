
def crear_nodo(dato):
    return {
        "dato": dato,
        "izquierdo": None,
        "derecho": None
    }


def buscar_nodo(nodo, nombre):
    if nodo is None:
        return None

    if nodo["dato"] == nombre:
        return nodo

    encontrado = buscar_nodo(nodo["izquierdo"], nombre)

    if encontrado is not None:
        return encontrado

    return buscar_nodo(nodo["derecho"], nombre)

def agregar_nodo(raiz):
    nombre = input("Nombre del nuevo nodo: ")

    if buscar_nodo(raiz, nombre) is not None:
        print("Ese nodo ya existe.")
        return

    padre = input("Nombre del nodo padre: ")
    nodo_padre = buscar_nodo(raiz, padre)

    if nodo_padre is None:
        print("El nodo padre no existe.")
        return

    lado = input("Lado (izquierdo/derecho): ").lower()

    if lado not in ("izquierdo", "derecho"):
        print("Lado no válido.")
        return

    if nodo_padre[lado] is not None:
        print("Ese lado ya está ocupado.")
        return

    nodo_padre[lado] = crear_nodo(nombre)
    print("Nodo agregado correctamente.")


def recorrer(nodo):
    if nodo is not None:
        print(nodo["dato"])
        recorrer(nodo["izquierdo"])
        recorrer(nodo["derecho"])


raiz = crear_nodo("A")

while True:
    print("\n1. Agregar nodo")
    print("2. Mostrar recorrido")
    print("3. Salir")

    opcion = input("Seleccione: ")

    if opcion == "1":
        agregar_nodo(raiz)

    elif opcion == "2":
        recorrer(raiz)

    elif opcion == "3":
        break

    else:
        print("Opción inválida.")
