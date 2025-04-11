import pandas as pd

def read_parsing_table(csv_file):
    """
    Lee la tabla de análisis desde un archivo CSV y la convierte en un diccionario.
    
    Parámetros:
        csv_file (str): Ruta al archivo CSV que contiene la tabla de análisis.
        
    Retorna:
        dict: Tabla de análisis en el formato {no_terminal: {terminal: lista_producción}}
    """
    # Leer el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Inicializar el diccionario de la tabla de análisis
    parsing_table = {}
    
    # Iterar sobre cada fila del DataFrame
    for _, row in df.iterrows():
        non_terminal = row['NonTerminal']
        terminal = row['Terminal']
        production = row['Production']
        
        # Inicializar el diccionario del no terminal si aún no existe
        if non_terminal not in parsing_table:
            parsing_table[non_terminal] = {}
        
        # Convertir la producción en una lista
        if pd.isna(production) or production.strip() == "":
            production_list = []  # Producción épsilon
        else:
            production_list = production.split()  # Separar símbolos por espacios
        
        # Agregar la regla a la tabla de análisis
        parsing_table[non_terminal][terminal] = production_list
    
    return parsing_table

def predictive_parser(input_tokens, csv_file="parsing_table.csv"):
    """
    Implementa un analizador predictivo usando una tabla de análisis leída desde un archivo CSV.
    
    Parámetros:
        input_tokens (list): Lista de tokens de entrada a analizar.
        csv_file (str): Ruta al archivo CSV que contiene la tabla de análisis.
    """
    # Leer la tabla de análisis desde el archivo CSV
    parsing_table = read_parsing_table(csv_file)
    
    # Inicializar la pila y la entrada
    stack = ['$', 'E']
    input_tokens = input_tokens.copy()  # Evitar modificar la lista original
    input_tokens.append('$')
    pointer = 0
    
    # Imprimir encabezado del trazo del análisis
    print(f"{'Pila':<20} {'Entrada':<20} {'Acción'}")
    print("-" * 60)
    
    while stack:
        top = stack.pop()
        current_input = input_tokens[pointer]
        
        # Imprimir el estado actual
        print(f"{' '.join(stack[::-1]):<20} {' '.join(input_tokens[pointer:]):<20}", end=" ")
        
        # Verificar aceptación
        if top == current_input == '$':
            print("ACEPTAR")
            break
        
        # Manejar terminales
        elif top in ['int', '+', '*', '(', ')', '$']:
            if top == current_input:
                print("terminal")
                pointer += 1
            else:
                print("ERROR: desajuste de terminal")
                break
        
        # Manejar no terminales
        elif top in parsing_table:
            rule = parsing_table[top].get(current_input)
            if rule is not None:
                if rule:  # Producción no épsilon
                    stack.extend(reversed(rule))
                    print(f"{' '.join(rule)}")
                else:  # Producción épsilon
                    print("ε")
            else:
                print("ERROR: no se encontró regla")
                break
        else:
            print(f"ERROR: símbolo desconocido {top}")
            break
def procesar_tabla_analisis(archivo_entrada, archivo_salida):
    # Leer el archivo CSV de entrada
    df = pd.read_csv(archivo_entrada)
    
    # Extraer la lista de terminales (primera fila, excluyendo "Non-Terminal")
    terminales = df.columns[1:].tolist()
    
    # Lista para almacenar las producciones resultantes
    producciones = []
    
    # Iterar sobre cada fila (no terminales)
    for _, fila in df.iterrows():
        no_terminal = fila['Non-Terminal']
        
        # Iterar sobre cada terminal
        for terminal in terminales:
            produccion = fila[terminal]
            
            # Saltar celdas vacías o NaN
            if pd.isna(produccion) or produccion == '':
                continue
                
            # Reemplazar ε con cadena vacía
            if produccion == 'ε':
                produccion = ''
                
            # Agregar a la lista de producciones
            producciones.append({
                'NonTerminal': no_terminal,
                'Terminal': terminal,
                'Production': produccion
            })
    
    # Crear DataFrame con las producciones
    df_salida = pd.DataFrame(producciones)
    
    # Guardar en archivo CSV
    df_salida.to_csv(archivo_salida, index=False)
    print(f"Archivo generado exitosamente: {archivo_salida}")

# Ejecutar el analizador con esta entrada
if __name__ == "__main__":
    archivo_entrada = 'tabla.csv'
    archivo_salida = 'producciones.csv'
    procesar_tabla_analisis(archivo_entrada, archivo_salida)
    input_string = ['int', '+', 'int']
    predictive_parser(input_string, csv_file="producciones.csv")
