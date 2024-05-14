from Menus.menu_admin import *

def crear_producto(datos_productos:dict):
    productos = {}
    producto = ""
    opcion = 0
    index = -1
    print("\nSeleccione el tipo de producto:\n")
    print("Productos:\n")
    print("1. Celular")
    print("2. Computador")
    print("3. Televisor\n")
    
    opcion = pedir_opcion()

    if opcion == 1:
        producto = "celular"
        index = 0
    elif opcion == 2:
        producto = "computador"
        index = 1
    elif opcion ==3:
        producto = "televisor"
        index = 2
    
    if producto == "" or (opcion<0 or opcion>3):
        return datos_productos
    
    productos["identificacion"] = input("Ingrese el número de referencia del producto: ")
    productos["nombre"] = input("Ingrese el nombre del producto: ")
    productos["marca"] = input("Ingrese la marca del producto: ")
    productos["caracteristica"] = input("Ingrese la caracteristica del producto: ")
    productos["precio"] = float(input("Ingrese el precio: "))
    productos["cantidad"] = int(input("Ingrese la cantidad: "))

    datos_productos["productos"][index][producto].append(productos)
    print("\nProducto creado exitosamente")
    return datos_productos


def actualiza_producto(datos:dict):
    productos = {}
    tipo_producto = int(input("Digite el tipo de producto: \n1. Celular.\n2. Computador.\n3. Televisor"))

    if tipo_producto < 0 or tipo_producto >3:
        return datos
    
    if tipo_producto == 1:
        index = 0
        producto = "celular"

    elif tipo_producto == 2:
        producto = "computador"
        index = 1

    elif tipo_producto == 3:
        producto = "televisor"
        index = 2
    
    identificacion = input("Digite el número de identificación del producto: ")

    if datos["productos"][index][producto]["identificacion"] == identificacion:

        productos["nombre"] = input("Digite el nuevo nombre: ")
        productos["marca"] = input("Digite la marca: ")
        productos["caracteristica"] = input("Digite las caracteristicas: ")
        productos["precio"] = input("Digite el precio: ")
        productos["cantidad"] = input("Digite el cantidad del producto: ")

        if productos["nombre"] == datos["productos"][index][producto]["nombre"]:
            print("Deben ser diferentes")
            return datos

        if productos["marca"] == datos["productos"][index][producto]["marca"]:
            print("Deben ser diferentes")
            return datos
        
        
        if productos["caracteristica"] == datos["productos"][index][producto]["caracteristica"]:
            print("Deben ser diferentes")
            return datos
        
        if productos["precio"] == datos["productos"][index][producto]["precio"]:
            print("Deben ser diferentes")
            return datos
        
        if productos["cantidad"] == datos["productos"][index][producto]["cantidad"]:
            print("Deben ser diferentes")
            return datos

        datos["productos"][index][producto].update(producto)
        return datos
    print("Usuario no se ha podido encontrar")
    
    return datos

def elimina_producto(datos:dict):
    opcion = 0
    producto = ""
    identificador = input("Digita el número de referencia del producto: ")

    tipo_producto = input("Introduce el tipo de producto que es: ").lower() 

    if tipo_producto == "celular":
        producto = "celular"
        index = 0
    elif tipo_producto == "computador":
        producto = "computador"
        index = 1
    elif tipo_producto == "televisor":
        producto = "televisor"
        index = 2


    for i in range(len(datos["productos"][index][producto])):
        if datos["productos"][index][producto][i]["identificacion"] == identificador:

            opcion = int(input("¿Deseas eliminar de manera permanente? (1. Si \ 2. No):\n-> "))

            if opcion == 1:
                datos["productos"][index][producto].pop(index)
                print("Producto Eliminado")

                return datos

    return datos


def mostrar_producto(datos: dict):
    producto = input("Ingrese el producto: ")
    identificador = input("Ingrese la referencia del producto: ")

    print("\n*****************************************************")

    for i in range(len(datos["productos"])):
        if producto in datos["productos"][i]:
            for j in range(len(datos["productos"][i][producto])):
                if datos["productos"][i][producto][j]["identificacion"] == identificador:
 
                    return f"{datos['productos'][i][producto][j]['identificacion']} -> {datos['productos'][i][producto][j]['nombre']} \nMarca: {datos['productos'][i][producto][j]['marca']} \nCaracterísticas: {datos['productos'][i][producto][j]['caracteristica']} \nPrecio: {datos['productos'][i][producto][j]['precio']} \nCantidad: {datos['productos'][i][producto][j]['cantidad']}"

    return "No se ha podido conseguir el producto"
    
def listado_productos(datos: dict):

    celular = datos["productos"][0]["celular"]
    computador = datos["productos"][1]["computador"]
    televisor = datos["productos"][2]["televisor"]

    print("\n*****************************************************")
    print("\n*--PRODUCTOS--*\n")
    print("*****************************************************\n")
    print("PRODUCTO: Celular")
    ("*****************************************************\n")

    for i in range(len(celular)):
        print("--------------------------------------------------\n")
        print(f"Identificación: {celular[i]["identificacion"]}")
        print(f"Marca: {celular[i]["nombre"]}")
        print(f"Caracteristica(s): {celular[i]["marca"]}")
        print(f"Precio: {celular[i]["precio"]}")
        print(f"Cantidad: {celular[i]["cantidad"]}")

    print("\n*****************************************************")
    print("PRODUCTO: Computador")
    print("*****************************************************\n")

    for i in range(len(computador)):
        print("--------------------------------------------------\n")
        print(f"Identificación: {computador[i]["identificacion"]}")
        print(f"Marca: {computador[i]["nombre"]}")
        print(f"Caracteristica(s): {computador[i]["marca"]}")
        print(f"Precio: {computador[i]["precio"]}")
        print(f"Cantidad: {computador[i]["cantidad"]}")

    print("\n*****************************************************")
    print("PRODUCTO: Televisor")
    print("*****************************************************\n")

    for i in range(len(televisor)):
        print("--------------------------------------------------\n")
        print(f"Identificación: {televisor[i]["identificacion"]}")
        print(f"Marca: {televisor[i]["nombre"]}")
        print(f"Caracteristica(s): {televisor[i]["marca"]}")
        print(f"Precio: {televisor[i]["precio"]}")
        print(f"Cantidad: {televisor[i]["cantidad"]}")

    print()