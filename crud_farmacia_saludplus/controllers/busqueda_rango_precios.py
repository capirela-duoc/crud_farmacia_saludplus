from utils.utils import validar_entero_mayor_cero

def busqueda_rango_precios(dicc_descriptivo, dicc_operativo):
    try:
        if not dicc_descriptivo or not dicc_operativo or len(dicc_descriptivo) == 0 :
            print('No hay registros en nuestro sistema. Volverá al menú principal.')
            return
        
        precio_min = 0
        precio_max = 0
        
        print('Para buscar un medicamento por rango de precios favor ingrese: ')

        while True:
            precio_min = validar_entero_mayor_cero(int(input('Precio mínimo: ')))
            
            if precio_min is None:
                print('Erro al ingresar el rango mínimo de precio. Favor intente de nuevo')
            else:
                break
            
                    
        while True:
            precio_max = validar_entero_mayor_cero(int(input('Precio máximo: ')))
            
            if precio_max is None:
                print('Erro al ingresar el rango máximo de precio. Favor intente de nuevo')
            else:
                break
            
        for codigo in dicc_operativo:
            if dicc_operativo[codigo][0] >= precio_min and dicc_operativo[codigo][0] <= precio_max:
                print(f'Medicamento: {dicc_descriptivo[codigo][0]}')
            else:
                print('No existen medicamentos dentro de ese rango.')
        return
        
    except ValueError as error:
        print(f'Ha ocurrido un error en el sistema. Error: {error}')