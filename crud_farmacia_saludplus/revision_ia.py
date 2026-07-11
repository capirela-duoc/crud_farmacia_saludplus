# =====================================================================
# SOLUCIÓN EXAMEN TRANSVERSAL: FARMACIA SALUDPLUS
# =====================================================================

# ---------------------------------------------------------------------
# 3. FUNCIONES MÍNIMAS ESPERADAS Y VALIDACIONES
# ---------------------------------------------------------------------

def mostrar_menu():
    """Muestra las seis opciones del menú."""
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de medicamentos por rango de precio")
    print("3. Actualizar precio de medicamento")
    print("4. Agregar medicamento")
    print("5. Eliminar medicamento")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    """Lee un entero entre 1 y 6, usa try/except y retorna la opción validada."""
    try:
        opcion = int(input("Favor elija una de las opciones para continuar: "))
        if 1 <= opcion <= 6:
            return opcion
        else:
            return None
    except ValueError:
        return None


def buscar_codigo(diccionario, codigo):
    """Retorna True si el código existe; False si no existe. No distingue mayúsculas."""
    for clave in diccionario:
        if clave.upper() == codigo.upper():
            return True
    return False


# --- Funciones de validación independientes (Retornan True o False) ---
def validar_texto(texto):
    """Valida que el string no esté vacío ni contenga solo espacios."""
    if texto and texto.strip() != "":
        return True
    return False


def validar_entero_mayor_cero(valor):
    """Valida que el número entero sea mayor que cero."""
    if valor > 0:
        return True
    return False


def validar_entero_mayor_igual_cero(valor):
    """Valida que el número entero sea mayor o igual a cero."""
    if valor >= 0:
        return True
    return False


def validar_receta(opcion):
    """Valida que el ingreso para receta sea únicamente 's' o 'n'."""
    if opcion.lower() in ['s', 'n']:
        return True
    return False


# --- Funciones operativas de los controladores ---

def unidades_categoria(dicc_descriptivo, dicc_operativo, categoria_buscar):
    """Acumula unidades según categoría y muestra el total."""
    cantidad_unidades = 0
    # Recorremos el diccionario descriptivo
    for codigo in dicc_descriptivo:
        # Índice 1 corresponde a la categoría terapéutica
        if dicc_descriptivo[codigo][1].lower() == categoria_buscar.lower():
            # Acumulamos desde el diccionario operativo (Índice 1 son las unidades)
            cantidad_unidades += dicc_operativo[codigo][1]
            
    print(f"Cantidad total de unidades para la categoría '{categoria_buscar}': {cantidad_unidades}")


def busqueda_precio(dicc_descriptivo, dicc_operativo, precio_min, precio_max):
    """Busca medicamentos dentro de un rango de precio, con disponibilidad distinta de cero, 

    y muestra la lista ordenada.
    """
    resultados = []
    
    for codigo in dicc_operativo:
        precio_actual = dicc_operativo[codigo][0]
        stock_actual = dicc_operativo[codigo][1]
        
        # Validación lógica estricta: Rango inclusivo (AND) y stock mayor a cero
        if precio_min <= precio_actual <= precio_max and stock_actual > 0:
            nombre_med = dicc_descriptivo[codigo][0]
            # Guardamos como tupla (precio, nombre) para poder ordenar por precio de forma nativa
            resultados.append((precio_actual, nombre_med))
            
    if resultados:
        resultados.sort()  # Muestra la lista ordenada de menor a mayor precio
        print("\n--- Medicamentos Encontrados ---")
        for precio, nombre in resultados:
            print(f"$ {precio} -> {nombre}")
    else:
        print("No se encontraron medicamentos con stock disponible en ese rango de precios.")


def actualizar_precio(dicc_descriptivo, dicc_operativo, codigo, nuevo_precio):
    """Actualiza precio si el código existe. Retorna True o False."""
    if buscar_codigo(dicc_descriptivo, codigo) and validar_entero_mayor_cero(nuevo_precio):
        dicc_operativo[codigo.upper()][0] = nuevo_precio
        return True
    return False


def agregar_medicamento(dicc_descriptivo, dicc_operativo, codigo, nombre, categoria, laboratorio, dosis, receta, formato, precio, unidades):
    """Agrega un nuevo medicamento en ambos diccionarios de forma relacionada. Retorna True o False."""
    # Como la validación se hace en el flujo principal, aquí insertamos directamente
    dicc_descriptivo[codigo] = [nombre, categoria, laboratorio, dosis, receta, formato]
    dicc_operativo[codigo] = [precio, unidades]
    return True


def eliminar_medicamento(dicc_descriptivo, dicc_operativo, codigo):
    """Elimina un medicamento de ambos diccionarios. Retorna True o False."""
    if buscar_codigo(dicc_descriptivo, codigo):
        # Eliminamos de ambos diccionarios usando la clave correspondiente
        dicc_descriptivo.pop(codigo.upper())
        dicc_operativo.pop(codigo.upper())
        return True
    return False


# ---------------------------------------------------------------------
# PROGRAMA PRINCIPAL (main)
# ---------------------------------------------------------------------

def main():
    # 1. Diccionarios iniciales requeridos por la guía
    medicamentos = {
        'MED001': ['Paracetamol Plus', 'analgesico', 'LabVida', 500, False, 'tabletas'], 
        'MED002': ['Amoxicilina Forte', 'antibiotico', 'BioMed', 875, True, 'capsulas'], 
        'MED003': ['Vitamina C Max', 'suplemento', 'NutriLab', 1000, False, 'comprimidos'], 
        'MED004': ['Ibuprofeno Fast', 'analgesico', 'DolorOff', 400, False, 'tabletas']
    }
    
    inventario = {
        'MED001': [3990, 50], 
        'MED002': [8990, 12], 
        'MED003': [6990, 0], 
        'MED004': [4990, 30]
    }
    
    while True:
        mostrar_menu()
        opMenu = leer_opcion()
        
        if opMenu is None:
            print("Error: La opción ingresada no es válida. Debe ser un entero entre 1 y 6.")
            continue
            
        # Opción 1: Unidades por categoría
        if opMenu == 1:
            categoria_in = input("Favor ingrese categoría a validar: ")
            unidades_categoria(medicamentos, inventario, categoria_in)
            
        # Opción 2: Búsqueda por rango de precio
        elif opMenu == 2:
            try:
                p_min = int(input("Precio mínimo: "))
                p_max = int(input("Precio máximo: "))
                busqueda_precio(medicamentos, inventario, p_min, p_max)
            except ValueError:
                print("Error: Los límites de precio deben ser números enteros.")
                
        # Opción 3: Actualizar precio de medicamento
        elif opMenu == 3:
            cod = input("Favor ingrese código de medicamento a actualizar: ").upper()
            try:
                nuevo_p = int(input("Favor ingrese nuevo precio: "))
                # Invocamos la función y el programa principal decide el mensaje según True o False
                if actualizar_precio(medicamentos, inventario, cod, nuevo_p):
                    print("Éxito: El precio ha sido actualizado correctamente.")
                else:
                    print("Error: El código no existe o el precio no cumple con las restricciones.")
            except ValueError:
                print("Error: El precio debe ser un número entero.")
                
        # Opción 4: Agregar medicamento
        elif opMenu == 4:
            print("\n--- Formulario de Registro de Medicamento ---")
            nombre = input("Ingrese nombre del medicamento: ")
            categoria = input("Ingrese la categoria del medicamento: ")
            laboratorio = input("Ingrese el laboratorio del medicamento: ")
            
            try:
                dosis = int(input("Ingrese dosis en mg del medicamento: "))
                receta_str = input("¿Requiere receta médica? (s/n): ")
                formato = input("Ingrese formato del medicamento: ")
                precio = int(input("Favor ingrese precio del medicamento: "))
                unidades = int(input("Favor cantidad de unidades disponibles: "))
                
                # Se valida cada campo de manera estrictamente independiente antes de llamar a la función
                if (validar_texto(nombre) and validar_texto(categoria) and validar_texto(laboratorio) and 
                    validar_entero_mayor_cero(dosis) and validar_receta(receta_str) and validar_texto(formato) and 
                    validar_entero_mayor_cero(precio) and validar_entero_mayor_igual_cero(unidades)):
                    
                    # Generamos una clave única autoincremental de forma segura
                    nuevo_codigo = f"MED{len(medicamentos) + 1:03d}"
                    receta_bool = True if receta_str.lower() == 's' else False
                    
                    if agregar_medicamento(medicamentos, inventario, nuevo_codigo, nombre, categoria, laboratorio, dosis, receta_bool, formato, precio, unidades):
                        print(f"Éxito: Medicamento registrado correctamente con el código {nuevo_codigo}.")
                    else:
                        print("Error: No se pudo agregar el medicamento en el sistema.")
                else:
                    print("Error: Uno o más datos ingresados no cumplen con las restricciones de formato o rango.")
            except ValueError:
                print("Error: Los campos numéricos (dosis, precio, unidades) deben ser enteros válidos.")
                
        # Opción 5: Eliminar medicamento
        elif opMenu == 5:
            cod = input("Ingrese código de producto que desea eliminar: ").upper()
            # El programa principal decide el mensaje según el retorno booleano
            if eliminar_medicamento(medicamentos, inventario, cod):
                print(f"Éxito: Producto con código {cod} eliminado exitosamente de ambos registros.")
            else:
                print("Error: El código ingresado no coincide con nuestros registros.")
                
        # Opción 6: Salir
        elif opMenu == 6:
            print("Programa finalizado.")
            break


# Punto de entrada estándar de ejecución
if __name__ == "__main__":
    main()