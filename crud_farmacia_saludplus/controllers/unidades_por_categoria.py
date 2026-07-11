from utils.utils import validar_texto

def unidades_por_categoria(dicc_descriptivo, dicc_operativo):
    while True:
        if not dicc_descriptivo or not dicc_operativo:
            return None
        else: 
            categoria = validar_texto(input('Favor ingrese categoría a validar: ').lower())
            cantidad_unidades = 0
            
            if categoria is None:
                print('Ha ocurrido un error al ingresar la cateoría. Favor intente de nuevo.')
            else:
                for elemento in dicc_descriptivo:
                    if categoria == dicc_descriptivo[elemento][5]:
                        cantidad_unidades += dicc_operativo[elemento][1]
                    
                print(f'Cantidad de unidades por categoria: {cantidad_unidades}')
                return
            
            
