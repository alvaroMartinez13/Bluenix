from Cliente.cliente import *
from Menus.menu_admin import *
from Menus.menu_cliente import *
from Menus.menu_cliente import *
from Menus.menu_cliente import menu_registro_gestión

def opcion_gestion_cliente(datos_cliente, opcion = 0):
    while True:
        try:     
            menu_gestion_usuarios()
            opcion = pedir_opcion()
            if opcion == 1:
                menu_opcion_gestion_usuarios(datos_cliente)
            elif opcion == 2:
                print("¡¡En mantenimiento, vuelva pronto!!")
            elif opcion == 3:
                print("¡¡En mantenimiento, vuelva pronto!!") 
            elif opcion == 4:
                print("¡¡En mantenimiento, vuelva pronto!!") 
            elif opcion == 5:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")

def menu_opcion_gestion_usuarios(datos_cliente, opcion = 0):

    while True:
        try:        
            menu_registro_gestión()
            opcion = pedir_opcion()
            if opcion == 1:
                datos_cliente = crear_usuario(datos_cliente)
            elif opcion ==2:
                datos_cliente = actualiza_usuario(datos_cliente) 
            elif opcion ==3:
                datos_cliente = elimina_usuario(datos_cliente)
            elif opcion ==4:
                print(mostrar_usuario(datos_cliente))
            elif opcion ==5:
                listado_clientes(datos_cliente)
            elif opcion ==6:
                break
        except Exception as e:
            registrar_error(e)
            print("Error durante la ejecución. Revisar el log de errores.")
        
