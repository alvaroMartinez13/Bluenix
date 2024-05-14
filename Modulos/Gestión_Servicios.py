
from Menus.menu_admin import *
from Servicios.servicios import *


def opcion_gestion_servicios(datos_servicio, opcion = 0):
    while True:
        try:
            menu_gestion_servicios()
            opcion = pedir_opcion() 
            if opcion == 1:
                datos_servicio = crear_servicio(datos_servicio)
            elif opcion ==2:
                datos_servicio = actualiza_servicio(datos_servicio) 
            elif opcion ==3:
                datos_servicio = elimina_servicio(datos_servicio)
            elif opcion ==4:
                print(mostrar_servicio(datos_servicio)) 
            elif opcion ==5:
                listado_servicios(datos_servicio) 
            elif opcion ==6:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")