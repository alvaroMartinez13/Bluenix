from Menus.menu_admin import *

def crear_servicio(datos:dict):
    servicio = {}
    try:
        servicio["tipo_servicio"] = input("Ingrese el tipo de Servicio: ")
        servicio["Caracteristicas"] = input("Ingrese las caracteristicas del Servicio: ")
        servicio["precio"] = float(input("Ingrese el precio del Servicio: "))
        servicio["estado"] = True
        servicio["popularidad"] = 0
        datos["servicios"].append(servicio)
        print("\nservicio creado exitosamente")
        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def actualiza_servicio(datos:dict):
    servicio = {}
    opcion = 0
    tipo_servicio = ""
    try:
        print("Selecciona que opción desea modificar: \n1. tipo de servicio.\n2. Caracteristicas. \n3. Precio. \n4. Estado del servicio.\n")
        opcion = pedir_opcion()
        tipo_servicio = input("Digite el Servicio que desea modificar: ")
        if opcion == 1:
            for i in range(len(datos["servicios"])):
                if datos["servicios"][i]["tipo_servicio"] == tipo_servicio:
                    servicio["tipo_servicio"] = input("Ingrese el tipo de Servicio nuevo: ")
                    if datos["servicios"][i]["tipo_servicio"] == servicio["tipo_servicio"]:
                        print("Deben ser diferentes los tipos")
                        return datos
            datos["servicios"][i].update(servicio)
            return datos

        elif opcion == 2:
            for i in range(len(datos["servicios"])):
                if datos["servicios"][i]["tipo_servicio"] == tipo_servicio:
                    servicio["caracteristicas"] = input("Digite las nuevas caracteristicas: ")
                    if datos["servicios"][i]["caracteristicas"] == servicio["caracteristicas"]:
                        print("Deben ser diferentes las características")
                        return datos
            servicio["Caracteristicas"] = input("Ingrese las caracteristicas del Servicio: ")
            datos["servicios"][i].update(servicio)

        elif opcion == 3:
            for i in range(len(datos["servicios"])):
                if datos["servicios"][i]["tipo_servicio"] == tipo_servicio:
                    servicio["precio"] = float(input("Ingrese el precio del Servicio: "))
                    if datos["servicios"][i]["precio"] == servicio["precio"]:
                        print("Deben ser diferentes los precios")
                        return datos
            datos["servicios"][i].update(servicio)

        elif opcion == 4:
            for i in range(len(datos["servicios"])):
                if datos["servicios"][i]["tipo_servicio"] == tipo_servicio:
                    servicio["estado"] = bool("Desea tener:\n1. Activo el Servicio\n0. Desactivo el Servicio")
                    if datos["servicios"][i]["estado"] == servicio["estado"]:
                        print("Deben ser diferente estado")
                        return datos
            datos["servicios"][i].update(servicio)
        
        elif opcion<0 or  opcion>5:
            return datos
        
        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def elimina_servicio(datos:dict):
    opcion = 0
    try:
        tipo_servicio = input("Digite el Servicio que desea eliminar: ")
        for i in range(len(datos["servicios"])):
            if datos["servicios"][i]["tipo_servicio"] == tipo_servicio:
                print("¿Deseas eliminar el servicio?:\n1. Si\n2. No")
                opcion = pedir_opcion()
                if opcion == 1:
                    datos["servicios"].pop(i)

        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def mostrar_servicio(datos: dict):
    try:
        servicios = input("Ingrese el servicio: ")

        print("\n*****************************************************")

        for i in range(len(datos["servicios"])):
            if datos["servicios"][i]["tipo_servicio"] == servicios:
                return f"Nombre del Servicio: {datos['servicios'][i]['tipo_servicio']} \nCaracteristicas: {datos['servicios'][i]['Caracteristicas']} \nPrecio: {datos['servicios'][i]['precio']} \nEstado: {datos['servicios'][i]['estado']}"

        return "No se ha podido conseguir el servicio"
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def listado_servicios(datos: dict):
    try:
        print("\n*****************************************************")
        print("\n*--SERVICIOS--*\n")
        print("*****************************************************")
        print("--------------------------------------------------")
        for i in range(len(datos["servicios"])):
            print(f"Servicio: {datos["servicios"][i]["tipo_servicio"]}")
            print(f"Caracteristica(s): {datos["servicios"][i]["Caracteristicas"]}")
            print(f"Precio: {datos["servicios"][i]["precio"]}")
            print("--------------------------------------------------")
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")