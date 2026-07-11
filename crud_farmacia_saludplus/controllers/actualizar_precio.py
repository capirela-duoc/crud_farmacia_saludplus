from utils.utils import validar_texto, validar_opcion

def actualizar_precio(dicc_descriptivo, dicc_operativo):
    try:
        while True:
            codigo = validar_texto(input('Favor ingrese código de medicamento cuyo precio desea actualizar: ').upper())
        
            if codigo is None:
                print('Error al ingresar código de medicamento. Favor intente de nuevo.')
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