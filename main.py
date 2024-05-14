#Imports
from Modulos.Gestion_Usuarios import opcion_gestion_cliente
from Modulos.Gestión_Servicios import *
from config import *
from Menus.menu_admin import *
from Menus.menu_catalogo import *
from Cliente.cliente import *
from Servicios.servicios import *
from Productos.productos import *
from Modulos.ventas import *
from Menus.menu_ventas import *

#Constants
RUTA_CLIENTE = "Cliente/cliente.json"
RUTA_PRODUCTO = "Productos/productos.json"
RUTA_SERVICIO = "Servicios/servicios.json"
RUTA_FACTURA = "Reporte/facturacion.json"

#Variables
opcion = 0
try:
    datos_cliente = cargar_datos(RUTA_CLIENTE)
    datos_producto = cargar_datos(RUTA_PRODUCTO)
    datos_servicio = cargar_datos(RUTA_SERVICIO)
    datos_factura = cargar_datos(RUTA_FACTURA)
except Exception as e:
    registrar_error(e)
    print("Error al cargar los datos. Revisar el log de errores.")
    exit()

while True:
    try:
        menu_principal()
        opcion = pedir_opcion()
        if opcion == 1:
            opcion_gestion_cliente(datos_cliente)
        elif opcion == 2:
            opcion_gestion_servicios(datos_servicio)
        elif opcion == 3:
            opcion_menu_ventas(datos_cliente, datos_servicio, datos_producto)
        elif opcion == 4:
            print("¡¡En mantenimiento, vuelva pronto!!") 
        elif opcion == 5:
            print("Fin")
            break
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")

try:
    guardar_datos(datos_cliente, RUTA_CLIENTE)
    guardar_datos(datos_servicio, RUTA_SERVICIO)
    guardar_datos(datos_producto, RUTA_PRODUCTO)
    guardar_datos(datos_factura, RUTA_FACTURA)
except Exception as e:
    registrar_error(e)
    print("Error al guardar los datos. Revisar el log de errores.")