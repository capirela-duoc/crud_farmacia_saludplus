from utils.utils import validar_texto, validar_opcion, buscar_por_codigo

def actualizar_precio(dicc_descriptivo, dicc_operativo):
    try:
        if not dicc_descriptivo or not dicc_operativo or len(dicc_descriptivo) == 0 :
            print('No hay registros en nuestro sistema. Volverá al menú principal.')
            return
        while True:
            codigo = validar_texto(input('Favor ingrese código de medicamento cuyo precio desea actualizar: ').upper())
            
            if codigo is None:
                print('Error al ingresar el código del medicamento. Favor intente de nuevo.')
                
            if buscar_por_codigo(codigo, dicc_descriptivo) is None:
                print('El código ingresado no coincide con nuestros registros. Favor intente de nuevo')
                
            else:
                validar_actualizacion = validar_opcion(input((f'El precio del medicamento {dicc_descriptivo[codigo][0]} es de {dicc_operativo[codigo][0]}. ¿Está seguro que desea actualizar? S/N: ')))
                
                if validar_actualizacion:
                    precio = input('Favor ingrese nuevo precio: ')
                    
                    dicc_operativo[codigo][0] = precio
                    
                    print(f'El precio del medicamento "{dicc_descriptivo[codigo][0]}", ha sido actualizado correctamente a {dicc_operativo[codigo][0]}')
                    return
                else:
                    print('Usted ha elegido no actualizar el precio.')
                    return
    
    except ValueError as error:
        print(f'Ha ocurrido un error al actualizar el precio. Error: {error}')