import json

from Menus.menu_admin import registrar_error

def cargar_datos(archivo):
    try:
        datos = {}
        with open(archivo,"r") as file:
            datos=json.load(file)
        return datos
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")
        
        

def guardar_datos(datos, archivo):
    try:
        datos = dict(datos)
        
        diccionario=json.dumps(datos, indent=4)
        file=open(archivo,"w")
        file.write(diccionario)
        file.close()
    except Exception as e:
        registrar_error(e)
        print("Error durante la ejecución. Revisar el log de errores.")