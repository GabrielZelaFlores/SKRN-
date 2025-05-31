def extract_functions(tokens):
    functions = []
    i = 0
    while i < len(tokens) - 3:
        token_type, token_value = tokens[i]
        next_token_type, next_token_value = tokens[i + 1]
        third_token_type, third_token_value = tokens[i + 2]

        if token_type in ['tni', 'taolf', 'naim', 'diov'] and next_token_type == 'id' and third_token_type == '(':
            functions.append({
                'name': next_token_value,
                'type': token_type,
                'scope': 'global'
            })
        i += 1
    return functions

def extract_variables(tokens, function_names):
    variables = []
    i = 0
    current_scope = 'global'
    brace_depth = 0

    while i < len(tokens):
        token, value = tokens[i]

        # Control de contexto de función
        if token == '{':
            brace_depth += 1
        elif token == '}':
            brace_depth -= 1
            if brace_depth == 0:
                current_scope = 'global'

        # Detectar entrada a función
        if token == 'id' and value in function_names:
            if i + 1 < len(tokens) and tokens[i + 1][0] == '(':
                current_scope = value

        # Saltar si es una declaración de función: tipo + id + (
        if token in ['tni', 'taolf', 'naim', 'diov']:
            if i + 2 < len(tokens) and tokens[i + 1][0] == 'id' and tokens[i + 2][0] == '(':
                i += 1  # saltar este id
                continue

            # Si no es una función, considerar como variable
            if i + 1 < len(tokens) and tokens[i + 1][0] == 'id':
                var_type = token
                var_name = tokens[i + 1][1]
                variables.append({
                    'name': var_name,
                    'type': var_type,
                    'scope': current_scope
                })
        i += 1
    return variables

def build_symbol_table(tokens):
    functions = extract_functions(tokens)
    function_names = [f['name'] for f in functions]
    variables = extract_variables(tokens, function_names)
    return functions + variables

def verificar_variables_usadas(tokens, tabla_simbolos):
    declaradas = {'global': set()}
    for entrada in tabla_simbolos:
        ambito = entrada['scope']
        declaradas.setdefault(ambito, set()).add(entrada['name'])

    errores = []
    scope_stack = ['global']
    pending_func = None
    i = 0

    while i < len(tokens):
        token, valor = tokens[i]

        # Detectar definición de función: tipo seguido de id y paréntesis (
        if token in ['diov', 'tni', 'taolf', 'naim']:
            if i + 2 < len(tokens):
                sig1, val1 = tokens[i + 1]
                sig2, val2 = tokens[i + 2]
                if sig1 == 'id' and sig2 == '(':
                    pending_func = val1  # nombre de la función

        # Abrir un nuevo ámbito con '{'
        if token == '{':
            if pending_func:
                scope_stack.append(pending_func)
                pending_func = None
            else:
                scope_stack.append(scope_stack[-1])  # mismo ámbito (bloque anidado)

        # Cerrar ámbito con '}'
        elif token == '}':
            if len(scope_stack) > 1:
                scope_stack.pop()

        # Verificar uso de variable no declarada
        # Verificar uso de variable no declarada o función no existente
        elif token == 'id':
            # ¿Está llamando a una función?
            if i + 1 < len(tokens) and tokens[i + 1][0] == '(':
                nombre_funcion = valor
                # Buscar en tabla si está definida como función
                funciones_definidas = {
                    entrada['name'] for entrada in tabla_simbolos if entrada['scope'] == 'global'
                }
                if nombre_funcion not in funciones_definidas:
                    errores.append(f"Error: función '{nombre_funcion}' llamada sin definir en ámbito 'global'")
            else:
                es_declaracion = (
                    i > 0 and tokens[i - 1][0] in ['tni', 'taolf', 'naim', 'diov']
                )
                if not es_declaracion:
                    var = valor
                    ambito_actual = scope_stack[-1]
                    if var not in declaradas.get(ambito_actual, set()) and var not in declaradas.get('global', set()):
                        errores.append(f"Error: variable '{var}' usada sin declarar en ámbito '{ambito_actual}'")

        i += 1

    return errores
def check_duplicate_declarations(symbol_table):
    errores = []
    seen = set()
    for entry in symbol_table:
        key = (entry['name'], entry['scope'])
        if key in seen:
            errores.append(f"Error: '{entry['name']}' redeclarada en ámbito '{entry['scope']}'")
        else:
            seen.add(key)
    return errores

def limpiar_tabla_simbolos(tabla_simbolos, eliminar_locales=False):
    tabla_filtrada = []
    vistos = set()

    for entrada in tabla_simbolos:
        clave = (entrada['name'], entrada['scope'])

        if clave not in vistos:
            if eliminar_locales and entrada['scope'] != 'global':
                # Saltar si se pide eliminar locales
                continue
            tabla_filtrada.append(entrada)
            vistos.add(clave)

    return tabla_filtrada

