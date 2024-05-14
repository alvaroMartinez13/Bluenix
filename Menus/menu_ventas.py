from Menus.menu_admin import *
from Menus.menu_catalogo import *
from Modulos.ventas import *
from Productos.productos import *

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

def opcion_registro_ventas(datos_servicio, datos_producto, opcion = 0):
    while True:
        try:
            menu_catologo()
            opcion = pedir_opcion()
            if opcion == 1:
                seleccion1_registro_ventas()
            elif opcion == 2:
                ver_catalogo(datos_servicio, datos_producto)
            elif opcion == 3:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")

def seleccion1_registro_ventas(opcion = 0):
    while True:
        try:
            menu_registro_productos()
            opcion = pedir_opcion()
            if opcion == 1:
                datos_producto = crear_producto(datos_producto)
            elif opcion == 2:
                datos_producto = actualiza_producto(datos_producto)
            elif opcion == 3:
                datos_producto = elimina_producto(datos_producto)
            elif opcion == 4:
                print(mostrar_producto(datos_producto))
            elif opcion == 5:
                listado_productos(datos_producto)
            elif opcion == 6:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")

def opcion2_registro_ventas(datos_cliente, datos_servicio, datos_producto, opcion = 0):
    while True:
        try:
            print("Selecciona: \n1.Servicio. \n2.Producto. \n3.Salir")
            opcion = pedir_opcion()
            if opcion == 1:
                numero_factura = int(input("Digite el número de la facturación: "))
                datos_fatura = venta_servicio(datos_cliente, datos_servicio, numero_factura, datos_fatura)
            elif opcion ==2:
                numero_factura = int(input("Digite el número de la facturación: "))
                datos_fatura = venta_producto(datos_cliente, datos_producto, numero_factura, datos_fatura)
            elif opcion == 3:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")


def menu_registro_ventas():
    print("\n*****************************************************")
    print("Módulo: Ventas / Registro y Gestión del Usuarios\n")
    print("1. Realizar Venta")
    print("2. Ver Factura específica")
    print("3. Salir a Menú Ventas")
    print("\n*****************************************************\n")