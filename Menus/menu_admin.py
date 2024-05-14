import datetime


def menu_principal():
    print("\n*****************************************************")
    print("\nBienvenido a la Familia Claro\n")
    print("Módulos:")
    print("1. Gestión de Usuarios")
    print("2. Gestión de Servicios")
    print("3. Ventas")
    print("4. Reportes")
    print("5. Salir")
    print("\n*****************************************************\n")

def menu_gestion_usuarios():
    print("\n*****************************************************")
    print("Módulo: Gestión de Usuarios\n")
    print("1. Registro y Gestión de Usuarios")
    print("2. Historial de Usuarios")
    print("3. Personalización de Servicios")
    print("4. Gestión de las ventas")
    print("5. Salir a Menú Principal")
    print("\n*****************************************************\n")

def menu_gestion_servicios():
    print("\n*****************************************************")
    print("Módulo: Gestión de Servicios\n")
    print("1. Registrar Servicio")
    print("2. Actualizar Servicio")
    print("3. Eliminar Servicio")
    print("4. Mostrar Servicio")
    print("5. Lista de Servicios")
    print("6. Salir a Menú Principal")
    print("\n*****************************************************\n")

def menu_ventas():
    print("\n*****************************************************")
    print("Módulo: Ventas\n")
    print("1. Catalogo de servicios y productos")
    print("2. Registro de las ventas de Servicios y Productos")
    print("3. Salir a Menú Principal")
    print("\n*****************************************************\n")

def pedir_opcion():
    while True:
        try:
            opcion = int(input("Ingrese su opción: "))
            if opcion < 0:
                raise ValueError("La opción no puede ser negativa.")
            return opcion
        except ValueError as e:
            print("Error: Solo se permiten enteros positivos.")
            registrar_error(e)

def solicitar_dato(mensaje):
    valor = input(mensaje).strip()
    while valor == "":
        print("Este campo no puede estar vacío. Por favor, intente de nuevo.")
        valor = input(mensaje).strip()
    return valor

def registrar_error(error):
    now = datetime.datetime.now()
    fecha = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("errores.txt", "a") as file:
        file.write(f"{fecha} - Tipo de error: {type(error).__name__}, Mensaje: {error}\n")
