from Menus.menu_admin import *

def crear_usuario(datos:dict):
    usuario = {}
    usuario["nombre"] = solicitar_dato("Ingrese el nombre del usuario: ")
    usuario["identificacion"] = solicitar_dato("Ingrese el número de identificación del usuario: ")
    usuario["email"] = solicitar_dato("Ingrese el correo electrónico del usuario: ")
    usuario["celular"] = solicitar_dato("Ingrese el celular del usuario: ")
    usuario["direccion"] = solicitar_dato("Ingrese la dirección del usuario: ")
    usuario["area geografica"] = solicitar_dato("Ingrese el área geográfica del usuario: ")
    usuario["categoria"] = "Nuevo Cliente"
    try:
        for i in datos["usuario"]:
            if usuario["identificacion"] == i["identificacion"]:
                print("No se ha podido crear el usuario, el usuario ya existe")
                return datos
        datos["usuario"].append(usuario)
        print("\nUsuario creado exitosamente")
    except Exception as e:
        registrar_error(e)
        print("Ocurrió un error. Por favor, intente de nuevo.")
    return datos

def actualiza_usuario(datos:dict):
    try:
        opcion = 0
        indetificador = solicitar_dato("Digite el número de indentificación del Usuario: ")
        for i in range(0, len(datos["usuario"])):
            if datos["usuario"][i]["identificacion"] == indetificador:
                print("Seleccione que desea modificar:")
                print("1. Identificacion")
                print("2. Nombre")
                print("3. Correo electronico")
                print("4. Celular")
                print("5. Direccion")
                print("6. Área geografica")
                print("7. Categoria")
                print("8. Todo lo anterior")
                opcion = pedir_opcion()
                if opcion == 1:
                    datos["usuario"][i]["identificacion"] = solicitar_dato("Ingrese su nuevo número de identificación del Usuario")
                elif opcion == 2:
                    datos["usuario"][i]["nombre"] = solicitar_dato("Ingrese el nuevo nombre del Usuario")
                elif opcion == 3:
                    datos["usuario"][i]["email"] = solicitar_dato("Ingrese el nuevo correo electronico del Usuario")
                elif opcion == 4:
                    datos["usuario"][i]["celular"] = solicitar_dato("Ingrese el nuevo correo electronico del Usuario")
                elif opcion == 5:
                    datos["usuario"][i]["direccion"] = solicitar_dato("Ingrese el nuevo correo electronico del Usuario")
                elif opcion == 6:
                    datos["usuario"][i]["area geografica"] = solicitar_dato("Ingrese el nuevo correo electronico del Usuario")
                elif opcion == 7:
                    datos["usuario"][i]["categoria"] = cambiar_categoria(datos["usuario"][i]["categoria"])
                elif opcion == 8:
                    datos = actualiza_todo_usuario(datos, i)
                else:
                    print("No se pudo actualizar al usuario")
                return datos
        print("Usuario no existente")
        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")


def actualiza_todo_usuario(datos:dict, index):
    usuario = {}
    try:
        usuario["nombre"] = input("Ingrese el nombre del usuario: ")
        usuario["email"] = input("Ingrese el correo electronico del usuario: ")
        usuario["celular"] = input("Ingrese el celular del usuario: ")
        usuario["direccion"] = input("Ingrese la dirección del usuario: ")
        usuario["area geografica"] = input("Ingrese el área geografica del usuario: ")
        usuario["categoria"] = cambiar_categoria(datos["usuario"][index]["categoria"])
        datos["usuario"][index].update(usuario)
        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def cambiar_categoria(categoria):
    aux = categoria
    opcion = 0
    try:
        print("Selecciona una opción:")
        print("1. Nuevo Cliente")
        print("2. Cliente Regular")
        print("3. Cliente Leal")
        opcion = pedir_opcion()
        if opcion == 1:
            if aux != "Nuevo Cliente":
                aux = "Nuevo Cliente"
            else:
                print("Categoria estado actual, debes seleccionar otra categoria")
        elif opcion == 2:
            if aux != "Cliente Regular":
                aux = "Cliente Regular"
            else:
                print("Categoria estado actual, debes seleccionar otra categoria")
        elif opcion == 3:
            if aux != "Cliente Leal":
                aux = "Cliente Leal"
            else:
                print("Categoria estado actual, debes seleccionar otra categoria")
        return aux
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def elimina_usuario(datos:dict):
    try:
        indetificador = input("Digita el número de identificación del usuario: ")
        for i in range(0, len(datos["usuario"])):
            if datos["usuario"][i]["identificacion"] == indetificador:
                datos["usuario"].pop(i)
                print("Usuario Eliminado")
                break
        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def mostrar_usuario(datos:dict):
    try:
        identificador = input("Ingrese el número de identificación: ")

        print("\n*****************************************************")

        for i in range(len(datos["usuario"])):
            if datos["usuario"][i]["identificacion"] == identificador:
    
                return f"Identificación: {datos['usuario'][i]['identificacion']} -> Nombre: {datos['usuario'][i]['nombre']} \nCorreo electronico: {datos['usuario'][i]['email']} \nCelular: {datos['usuario'][i]['celular']} \nDirección: {datos['usuario'][i]['direccion']} \nÁrea geográfica: {datos['usuario'][i]['area geografica']}"

        return "No se ha podido conseguir al usuario"
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def listado_clientes(datos: dict):
    try:
        print("\n*****************************************************")
        print("\n*--Usuarios--*\n")
        print("*****************************************************")
        print("--------------------------------------------------")
        for i in range(len(datos["usuario"])):
            print(f"Identificación: {datos["usuario"][i]["identificacion"]}")
            print(f"Nombre(s): {datos["usuario"][i]["nombre"]}")
            print(f"Correo electronico: {datos["usuario"][i]["email"]}")
            print(f"Celular: {datos["usuario"][i]["celular"]}")
            print(f"Dirección: {datos["usuario"][i]["direccion"]}")
            print(f"Área geográfica: {datos["usuario"][i]["area geografica"]}")
            print(f"Categoria: {datos["usuario"][i]["categoria"]}")
            print("--------------------------------------------------")
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")
