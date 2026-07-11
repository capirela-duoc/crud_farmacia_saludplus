from utils.utils import validar_texto, buscar_por_codigo, validar_opcion

def eliminar_medicamentos(dicc_descriptivo, dicc_operativo):    
    if not dicc_descriptivo or not dicc_operativo or len(dicc_descriptivo) == 0 :
            print('No hay registros en nuestro sistema. Volverá al menú principal.')
            return
    else:
        while True:
            codigo = validar_texto(input('Ingrese código de producto que desea eliminar: ').upper())
        
            if codigo is None:
                print('Error al ingresar el código del medicamento. Favor intente de nuevo.')
                
            if buscar_por_codigo(codigo, dicc_descriptivo) is None:
                print('El código ingresado no coincide con nuestros registros. Favor intente de nuevo')
                
            else:
                busqueda_codigo = buscar_por_codigo(codigo, dicc_operativo)
                if not busqueda_codigo:
                    print('El código ingresado no coincide connuestros registros. Favor intente de nuevo.')
                else:
                    medicamento = dicc_descriptivo[codigo][0]
                    opcion = validar_opcion(input(f'¿Está seguro desea eliminar el medicamento {medicamento} del sistema? S/N: '))
                    
                    if not opcion:
                        break
                    else:
                        dicc_descriptivo.pop(codigo)
                        dicc_operativo.pop(codigo)
                        
                        print(f"Producto con código {codigo} eliminado exitosamente.")
                        break 

                    
                    
            
    