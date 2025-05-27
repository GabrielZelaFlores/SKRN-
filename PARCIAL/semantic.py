class SymbolTable:
    def __init__(self):
        self.table = []
        self.scope_stack = []

    def enter_scope(self, scope_name):
        self.scope_stack.append(scope_name)

    def exit_scope(self):
        if self.scope_stack:
            self.scope_stack.pop()

    def current_scope(self):
        return '::'.join(self.scope_stack) if self.scope_stack else 'global'

    def declare(self, name, var_type):
        self.table.append({
            "name": name,
            "type": var_type,
            "scope": self.current_scope()
        })

    def is_declared(self, name):
        # Verifica si está declarado en algún scope visible
        scopes = ['::'.join(self.scope_stack[:i+1]) for i in range(len(self.scope_stack))]
        for scope in reversed(scopes):
            for entry in self.table:
                if entry['name'] == name and entry['scope'] == scope:
                    return True
        return False

    def print_table(self):
        print("Tabla de símbolos:")
        for entry in self.table:
            print(entry)

def semantic_analysis(node, symbol_table):
    if node is None:
        return

    # Entrar a nuevo ámbito si es un bloque o función
    if node.value in ('Block', 'Program'):
        symbol_table.enter_scope(node.value)
    
    # Función: fed id ( Params ) { Program }
    if node.value == 'FuncDecl':
        func_name = None
        params = []

        for child in node.children:
            if child.value == 'id':
                func_name = child.value  # Podrías usar child.children[0].value si es más profundo
            elif child.value == 'Params':
                params = collect_params(child)

        if func_name:
            symbol_table.declare(func_name, 'func')
            symbol_table.enter_scope(func_name)
            for param in params:
                symbol_table.declare(param, 'param')

    # Variable: VarDecl -> Type E
    if node.value == 'VarDecl':
        var_type = None
        var_name = None
        for child in node.children:
            if child.value == 'Type':
                var_type = child.children[0].value  # Ej: tni
            elif child.value == 'E':
                var_name = find_identifier(child)
        if var_name and var_type:
            symbol_table.declare(var_name, var_type)

    # Uso de variables: cuando hay un 'id' que no forma parte de declaración o función
    if node.value == 'id':
        if not symbol_table.is_declared(node.value):
            print(f"ERROR SEMÁNTICO: variable '{node.value}' no declarada en ámbito '{symbol_table.current_scope()}'")

    # Recorremos hijos
    for child in node.children:
        semantic_analysis(child, symbol_table)

    # Salir de ámbitos
    if node.value == 'FuncDecl':
        symbol_table.exit_scope()
    if node.value in ('Block', 'Program'):
        symbol_table.exit_scope()

def find_identifier(node):
    """Encuentra el primer 'id' válido dentro de una expresión o nodo E, F, etc."""
    if node.value == 'id':
        return node.value
    for child in node.children:
        result = find_identifier(child)
        if result:
            return result
    return None

def collect_params(node):
    """Extrae todos los parámetros (id) desde Params -> Param ParamsTail"""
    params = []

    def collect(n):
        if n.value == 'Param':
            for child in n.children:
                if child.value == 'id':
                    params.append(child.value)
        for child in n.children:
            collect(child)

    collect(node)
    return params


