from utils.utils import validar_texto, validar_entero_positivo, validar_entero_mayor_cero, validar_opcion, crear_codigo

def agregar_medicamento(dicc_descriptivo, dicc_operativo):
    nombre = ""
    categoria = ""
    laboratorio = ""
    dosis_mg = 0
    requiere_receta = False
    formato = ""
    precio = 0
    unidades = 0
        
    if not dicc_descriptivo or not dicc_operativo:
        return None
    else:
        try:
            while True:
                nombre = validar_texto(input('Ingrese nombre del medicamento: '))
                
                if not nombre:
                    print('Error al ingresar el nombre. Favor ingrese de nuevo')
                else:
                    break
            
            while True:
                categoria = validar_texto(input('Ingrese la categoria del medicamento: '))
                
                if not categoria:
                    print('Error al ingresar el categoria. Favor ingrese de nuevo')
                else:
                    break
                
            while True:
                laboratorio = validar_texto(input('Ingrese el laboratorio del medicamento: '))
                
                if not laboratorio:
                    print('Error al ingresar el laboratorio. Favor ingrese de nuevo')
                else:
                    break
                
            while True:
                dosis_mg = validar_entero_positivo(input('Ingrese dosis en mg del medicamento: '))
                
                if dosis_mg is None:
                    print('Error al ingresar las dosis del medicamento. Favor ingrese de nuevo')
                else:
                    break
            
            while True:
                requiere_receta = validar_opcion(input('Favor indique si el medicamento requiere receta. Ingrese "s" para si y "n" para no: ' ))
                
                if not requiere_receta or requiere_receta is None:
                     print('Error al ingresar condición de receta. Favor ingrese de nuevo')
                else:
                    break
                
            while True:
                formato = validar_texto(input('Ingrese formato del medicamento: '))
                
                if not formato:
                    print('Error al ingresar el formato. Favor ingrese de nuevo')
                else:
                    break
                
            while True:
                try:
                    precio = validar_entero_positivo(int(input('Favor ingrese precio del medicamento: ')))
                    
                    if precio is None:
                        print('Error al ingresar precio. Favor intente de nuevo')
                    else:
                        break
                
                except ValueError as error:
                    print(f'Ha ocurrido un error al ingresar el precio del medicamento. Error: {error}')
                    
            while True:
                try:
                    unidades = validar_entero_mayor_cero(int(input('Favor cantidad de unidades disponibles del medicamento: ')))
                    
                    if unidades is None:
                        print('Error las unidades. Favor intente de nuevo')
                    else:
                        break
                
                except ValueError as error:
                    print(f'Ha ocurrido un error al ingresar las unidades del medicamento. Error: {error}')
                    
            
            codigo = crear_codigo(dicc_descriptivo)
            
            if codigo is None: 
                print('Error al asignar código de medicamento.')
                return
            else:
                if categoria or nombre or categoria or laboratorio or dosis_mg or requiere_receta or formato or precio or unidades:
                    dicc_descriptivo[codigo] = [nombre, categoria, laboratorio, dosis_mg, requiere_receta, formato]
                    dicc_operativo[codigo] = [precio, unidades]
                    
                    print('Medicamento ingresado correctamente')
                    print(f'Descriptivo: {dicc_descriptivo}')
                    print(f'Operativo: {dicc_operativo}')
                        
                
        except ValueError as error:
            print(f'Ha ocurrido un error la ingresar el producto en sistema. Favor intente de nuevo. Error: {error}')
    
    