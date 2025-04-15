import pandas as pd

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def read_parsing_table(csv_file):
    df = pd.read_csv(csv_file)
    parsing_table = {}
    for _, row in df.iterrows():
        non_terminal = row['NonTerminal']
        terminal = row['Terminal']
        production = row['Production']
        if non_terminal not in parsing_table:
            parsing_table[non_terminal] = {}
        production_list = [] if pd.isna(production) or production.strip() == "" else production.split()
        parsing_table[non_terminal][terminal] = production_list
    return parsing_table

def predictive_parser(input_tokens, csv_file="producciones.csv"):
    parsing_table = read_parsing_table(csv_file)
    stack = [(TreeNode('$'), '$'), (TreeNode('E'), 'E')]
    input_tokens = input_tokens.copy()
    input_tokens.append('$')
    pointer = 0
    root = stack[-1][0]  # Raíz del árbol

    print(f"{'Pila':<20} {'Entrada':<20} {'Acción'}")
    print("-" * 60)

    while stack:
        print(f"{' '.join(s for _, s in stack[::-1]):<20} {' '.join(input_tokens[pointer:]):<20}", end=" ")
        top_node, top = stack.pop()
        current_input = input_tokens[pointer]

        if top == current_input == '$':
            print("ACEPTAR")
            break
        elif top in ['int', '+', '*', '(', ')', '$','ε']:
            if top == current_input:
                print("terminal")
                pointer += 1
            else:
                print("ERROR: desajuste de terminal")
                break
        elif top in parsing_table:
            rule = parsing_table[top].get(current_input)
            if rule is not None:
                print(f"{' '.join(rule) if rule else 'ε'}")
                for symbol in reversed(rule):
                    child = TreeNode(symbol)
                    top_node.children.append(child)
                    stack.append((child, symbol))
            else:
                print("ERROR: no se encontró regla")
                break
        else:
            print(f"ERROR: símbolo desconocido {top}")
            break

    return root

def procesar_tabla_analisis(archivo_entrada, archivo_salida):
    df = pd.read_csv(archivo_entrada)
    terminales = df.columns[1:].tolist()
    producciones = []
    for _, fila in df.iterrows():
        no_terminal = fila['Non-Terminal']
        for terminal in terminales:
            produccion = fila[terminal]
            if pd.isna(produccion) or produccion == '':
                continue
            if produccion == 'ε':
                produccion = ''
            producciones.append({
                'NonTerminal': no_terminal,
                'Terminal': terminal,
                'Production': produccion
            })
    df_salida = pd.DataFrame(producciones)
    df_salida.to_csv(archivo_salida, index=False)
    print(f"Archivo generado exitosamente: {archivo_salida}")

def generar_arbol_graphviz(node, filename="arbol_sintactico"):
    """Genera un archivo DOT para visualizar el árbol con Graphviz"""
    
    # Contadores para nodos únicos
    node_counter = 0
    dot_lines = ["digraph G {"]
    
    def build_graph(node, parent_id=None):
        nonlocal node_counter
        current_id = node_counter
        node_counter += 1
        
        # Añadir el nodo actual
        dot_lines.append(f'  node{current_id} [label="{node.value}"];')
        
        # Conectar con el padre si existe
        if parent_id is not None:
            dot_lines.append(f'  node{parent_id} -> node{current_id};')
        
        # Procesar hijos recursivamente
        for child in node.children:
            build_graph(child, current_id)
    
    # Construir el grafo
    build_graph(node)
    dot_lines.append("}")
    
    # Escribir el archivo DOT
    dot_filename = f"{filename}.dot"
    with open(dot_filename, "w") as f:
        f.write("\n".join(dot_lines))
    
    print(f"Archivo DOT generado: {dot_filename}")
if __name__ == "__main__":
    archivo_entrada = 'tabla.csv'
    archivo_salida = 'producciones.csv'
    procesar_tabla_analisis(archivo_entrada, archivo_salida)
    input_string = ['int', '+', 'int']
    root = predictive_parser(input_string, csv_file=archivo_salida)
    generar_arbol_graphviz(root)
