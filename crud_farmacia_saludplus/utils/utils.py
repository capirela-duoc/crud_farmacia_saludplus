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
    if opMenu is None or (opMenu < 1 or opMenu > len(menuLen)):
        return None
    else:
        return opMenu
        
def mostrar_menu(opciones_menu):
    print('')
    print('------MENU-----')
    for indice, op_menu in enumerate(opciones_menu):
        print(f'{indice+1}. {op_menu}')
    print('')

def validar_opcion(op):
    if not op:
        return None
    elif op.upper() == "S":
        return True
    else:
        return False
    
def crear_codigo(diccionario):
    if not diccionario or len(diccionario) == 0:
        return None
    else:
        diccionario_len = len(diccionario.items())+1
        
        codigo = f"MD{diccionario_len:03d}"
        
        buscar_codigo = buscar_por_codigo(codigo, diccionario)
        
        if not buscar_codigo:
            return codigo
        else:
            return None
    
def buscar_por_codigo(codigo, diccionario):
    if not codigo:
        return None
    else:
        for cdg in diccionario:
            if cdg == codigo:
                return True
        return False
    
