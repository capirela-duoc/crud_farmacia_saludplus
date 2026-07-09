def validar_texto(txt):
    if len(txt) == 0 or txt == "":
        return None
    else:
        return txt.strip()
    
def validar_entero_positivo(num):
    if num is None or num == 0:
        return None
    else:
        return num
    
def validar_entero_mayor_cero(num):
    if num is None or num < 0 or not num:
        return None
    else:
        return num
    
def leer_menu(opMenu, menuLen):
    try:
        if opMenu is None or (opMenu < 1 or opMenu > menuLen):
            return None
        else:
            return opMenu
    except ValueError as error:
        print(f"Ha ocurri un error al valdiar la opción del menú: {error}")
        
def mostrar_menu(opciones_menu):
    if not opciones_menu or len(opciones_menu) == 0:
        return None
    else:
        for