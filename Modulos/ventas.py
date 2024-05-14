from Menus.menu_ventas import menu_registro_ventas, opcion2_registro_ventas, opcion_registro_ventas
from Servicios.servicios import *
from Productos.productos import *


def opcion_menu_ventas(datos_cliente, datos_servicio, datos_producto, opcion = 0):
    while True:
        try:
            menu_ventas()
            opcion = pedir_opcion()
            if opcion == 1:
                opcion_registro_ventas(datos_servicio, datos_producto)
            elif opcion == 2:
                while True:
                    opcion = 0
                    menu_registro_ventas()
                    opcion = pedir_opcion()
                    if opcion == 1:
                        opcion2_registro_ventas(datos_cliente, datos_servicio, datos_producto)
                    elif opcion == 2:
                        print(2)
                    elif opcion == 3:
                        break
            elif opcion == 3:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")



def ver_catalogo(servicios, productos):
    try:
        print("\n*******************************************************\n")
        print("*---CATALOGO---*")
        ("\n*******************************************************\n")
        listado_servicios(servicios)
        listado_productos(productos)
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def venta_servicio(usuarios:dict, servicios:dict, numero_factura, datos_fatura:dict):
    opcion = 0
    factura = {}
    costo_anual = 0
    impuesto = 0.19
    semanas = 52
    meses = 12
    try:
        factura["numero_facturacion"] = numero_factura
        while True:
            listado_servicios(servicios)
            servicio = input("Ingrese el servicio de interés: ")
            for i in range(len(servicios)):
                if servicios["servicios"][i]["tipo_servicio"] == servicio:
                    documento = input("Digite el número de identificación del usuario: ")
                    for j in range(len(usuarios)):
                        if usuarios["usuario"][j]["identificacion"] == documento:
                            factura["usuario"] = {
                                "identificacion": documento,
                                "nombre": usuarios["usuario"][j]["nombre"]
                            }

                        print("¿Deseas pagar de manera: \n1. Mensual. \n2. Semanal.")
                        opcion = pedir_opcion()

                        costo_anual = servicios["servicios"][i]["precio"]
                        costo_total_con_impuesto = costo_anual * (1 + impuesto)

                        if opcion == 1:
                            factura["servicios"] = {
                                "tipo_servicio": servicio,
                                "Caracteristicas": servicios["servicios"][i]["Caracteristicas"],
                                "precio": servicios["servicios"][i]["precio"],
                                "tipo_pago":{
                                    "mensual": True,
                                    "semanal": False
                                }
                            }

                            factura["total_pagar"] = costo_total_con_impuesto / meses
                            datos_fatura["facturacion"].append(factura)

                            return datos_fatura
        

                        elif opcion == 2:
                            factura["servicios"] = {
                                "tipo_servicio": servicio,
                                "Caracteristicas": servicios["servicios"][i]["Caracteristicas"],
                                "precio": servicios["servicios"][i]["precio"],
                                "tipo_pago":{
                                    "mensual": False,
                                    "semanal": True
                                }
                            }
                            
                            factura["total_pagar"] = costo_total_con_impuesto / semanas
                            datos_fatura["facturacion"].append(factura)

                            return datos_fatura
        
            print("No se ha podido realizar la venta")
            return datos_fatura                        
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

def venta_producto(usuarios:dict, productos:dict, numero_factura, datos_fatura:dict):
    tipo = 0
    factura = {}
    producto_elegido = ""
    costo_anual = 0
    impuesto = 0.19
    semanas = 52
    meses = 12
    try:
        factura["numero_facturacion"] = numero_factura
        while True:
            listado_productos(productos)
            tipo = int(input("Ingrese que tipo de producto desea: \n1.celular. \n2.computador. \n3.televisor \n-> "))
            if tipo == 1:
                producto_elegido = "celular"
            elif tipo == 2:
                producto_elegido = "computador"
            elif tipo == 3:
                producto_elegido = "televisor"

            producto = input("Ingrese el producto de interés: ")
            opcion = 0
            for i in range(len(productos["productos"])):
                if producto_elegido in productos["productos"][i]:
                    for j in range(len(productos["productos"][i][producto_elegido])):
                        if productos["productos"][i][producto_elegido][j]["nombre"] == producto:
                            documento = input("Digite el número de identificación del usuario: ")
                            for j in range(len(usuarios)):
                                if usuarios["usuario"][j]["identificacion"] == documento:
                                    factura["usuario"] = {
                                        "identificacion": documento,
                                        "nombre": usuarios["usuario"][j]["nombre"]
                                    }

                                    cantidad = int(input(f"Digita la cantidad del {producto}: "))

                                    print("¿Deseas pagar de manera: \n1. Mensual. \n2. Semanal.")
                                    opcion = pedir_opcion()

                                    costo_anual = productos["productos"][i][producto_elegido][j]["precio"]
                                    costo_total_con_impuesto = (costo_anual*cantidad) * (1 + impuesto)

                                    if opcion == 1:
                                        factura["productos"] = {
                                            "tipo_producto": producto_elegido,
                                            "identificacion": productos["productos"][i][producto_elegido][j]["identificacion"],
                                            "nombre": producto,
                                            "marca": productos["productos"][i][producto_elegido][j]["marca"],
                                            "caracteristica": productos["productos"][i][producto_elegido][j]["marca"],
                                            "precio": productos["productos"][i][producto_elegido][j]["precio"],
                                            "cantidad": cantidad,
                                            "tipo_pago":{
                                                "mensual": True,
                                                "semanal": False
                                            }
                                        }

                                        factura["total_pagar"] = costo_total_con_impuesto / meses
                                        datos_fatura["facturacion"].append(factura)

                                        return datos_fatura
                    

                                    elif opcion == 2:
                                        factura["productos"] = {
                                            "tipo_producto": producto_elegido,
                                            "identificacion": productos["productos"][i][producto_elegido][j]["identificacion"],
                                            "nombre": producto,
                                            "marca": productos["productos"][i][producto_elegido][j]["marca"],
                                            "caracteristica": productos["productos"][i][producto_elegido][j]["marca"],
                                            "precio": productos["productos"][i][producto_elegido][j]["precio"],
                                            "cantidad": cantidad,
                                            "tipo_pago":{
                                                "mensual": True,
                                                "semanal": False
                                            }
                                        }
                                        
                                        factura["total_pagar"] = costo_total_con_impuesto / semanas
                                        datos_fatura["facturacion"].append(factura)

                                        return datos_fatura
                
            print("No se ha podido realizar la venta")
            return datos_fatura            
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")


