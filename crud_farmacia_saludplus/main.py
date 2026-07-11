from utils.utils import validar_texto, leer_menu, mostrar_menu
from controllers.agregar_medicamentos import agregar_medicamento
from controllers.unidades_por_categoria import unidades_por_categoria
from controllers.eliminar_medicamentos import eliminar_medicamentos
from controllers.actualizar_precio import actualizar_precio
from controllers.busqueda_rango_precios import busqueda_rango_precios

def main():
    try:
        medicamentos = {'MED001': ['Paracetamol Plus', 'analgesico', 'LabVida', 500, False, 'tabletas'], 'MED002': ['Amoxicilina Forte', 'antibiotico', 'BioMed', 875, True, 'capsulas'], 'MED003': ['Vitamina C Max', 'suplemento', 'NutriLab', 1000, False, 'comprimidos'], 'MED004': ['Ibuprofeno Fast', 'analgesico', 'DolorOff', 400, False, 'tabletas']}
        #medicamentos = {}
        inventario = {'MED001': [3990, 50], 'MED002': [8990, 12], 'MED003': [6990, 0], 'MED004': [4990, 30]}
        menu = ['Unidades por categoría', 'Búsqueda de medicamentos por rango de precio', 'Actualizar precio de medicamento', 'Agregar medicamento', 'Eliminar medicamento', 'Salir']
        opMenu = 0
        
        while opMenu != 6:
            mostrar_menu(menu)
            opMenu = leer_menu(int(input('Favor elija una de las opciones para continuar: ')), menu)
            
            if opMenu is None:
                print('La opción ingresada no coincide con nuestro sistema. favor intente de nuevo')
            else:
                match opMenu:
                    case 1:
                        unidades_por_categoria(medicamentos, inventario)  
                    case 2:
                        busqueda_rango_precios(medicamentos, inventario)
                    case 3:
                        actualizar_precio(medicamentos,inventario)
                    case 4:
                        agregar_medicamento(medicamentos, inventario)
                    case 5:
                        eliminar_medicamentos(medicamentos, inventario)
                    case 6:
                        print('Usted ha elegido salir del sistema!')
                        return
                    case _: 
                        print('La opción ingresada no coincide con nuestro sistema. Favor intente de nuevo.')
    except ValueError as error:
        print(f'Ha ocurrido un error en el sistema. Error: {error}')
main()