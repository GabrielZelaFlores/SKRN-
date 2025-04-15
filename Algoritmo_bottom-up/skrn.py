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
        top_node, top = stack.pop()
        current_input = input_tokens[pointer]
        print(f"{' '.join(s for _, s in stack[::-1]):<20} {' '.join(input_tokens[pointer:]):<20}", end=" ")

        if top == current_input == '$':
            print("ACEPTAR")
            break
        elif top in ['int', '+', '*', '(', ')', '$']:
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

def inorder_traversal(node):
    if not node.children:
        return [node.value]
    mid = len(node.children) // 2
    result = []
    for i, child in enumerate(node.children):
        if i == mid:
            result.append(node.value)
        result.extend(inorder_traversal(child))
    if mid == 0:
        result.insert(0, node.value)
    return result

def postorder_traversal(node):
    result = []
    for child in node.children:
        result.extend(postorder_traversal(child))
    result.append(node.value)
    return result

def guardar_recorridos(root, archivo="recorridos.csv"):
    inorden = inorder_traversal(root)
    postorden = postorder_traversal(root)
    df = pd.DataFrame({"inorden": inorden, "postorden": postorden})
    df.to_csv(archivo, index=False)
    print(f"Recorridos guardados en: {archivo}")

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

def imprimir_arbol(node, nivel=0):
    print("  " * nivel + f"- {node.value}")
    for child in node.children:
        imprimir_arbol(child, nivel + 1)

if __name__ == "__main__":
    archivo_entrada = 'tabla.csv'
    archivo_salida = 'producciones.csv'
    procesar_tabla_analisis(archivo_entrada, archivo_salida)
    input_string = ['int', '+', '+', 'int']
    root = predictive_parser(input_string, csv_file=archivo_salida)
    imprimir_arbol(root)
    guardar_recorridos(root, archivo="recorridos.csv")
