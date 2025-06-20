def extract_functions(tokens):
    functions = []
    i = 0
    while i < len(tokens) - 3:
        token_type, token_value = tokens[i]
        next_token_type, next_token_value = tokens[i + 1]
        third_token_type, third_token_value = tokens[i + 2]

        if token_type in ['tni', 'taolf', 'diov','gnirts','loob'] and next_token_type == 'id' and third_token_type == '(':
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
        if token in ['tni', 'taolf', 'diov','gnirts','loob']:
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
        if token in ['diov', 'tni', 'taolf','gnirts','loob']:
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
                    i > 0 and tokens[i - 1][0] in ['tni', 'taolf', 'naim', 'diov','gnirts','loob']
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

def inferir_tipo_literal(valor):
    try:
        if valor == 'eurt' or valor == 'eslaf':
            return 'loob'
        if valor.startswith('"') and valor.endswith('"'):
            return 'gnirts'
        if '.' in valor:
            float(valor)
            return 'taolf'
        if valor.isdigit():
            return 'tni'
    except:
        pass
    return None
def verificar_tipos_expresiones(tokens, tabla_simbolos):
    errores = []
    tipos_vars = {(entry['name'], entry['scope']): entry['type'] for entry in tabla_simbolos}
    scope_stack = ['global']
    i = 0
    while i < len(tokens):
        token, valor = tokens[i]

        # Cambio de ámbito
        if token == '{':
            scope_stack.append(scope_stack[-1])
        elif token == '}':
            if len(scope_stack) > 1:
                scope_stack.pop()

        # Asignación: buscamos patrón id = ...
        elif token == 'id' and i + 1 < len(tokens) and tokens[i + 1][0] == '=':
            nombre_var = valor
            ambito = scope_stack[-1]
            tipo_var = tipos_vars.get((nombre_var, ambito)) or tipos_vars.get((nombre_var, 'global'))

            if tipo_var is None:
                i += 1
                continue  # variable no declarada (ya lo maneja otra función)

            # Obtener los tokens a la derecha del "=" hasta el ";"
            i += 2
            expr_tokens = []
            while i < len(tokens):
                t, v = tokens[i]
                if t in ['tni', 'taolf', 'loob', 'gnirts', 'diov'] and (i + 1 < len(tokens) and tokens[i + 1][0] == 'id'):
                    break  # nueva declaración detectada
                if t == '=' and len(expr_tokens) == 0:
                    # ignora casos como: a = = 5 (doble igual mal escrito)
                    break
                expr_tokens.append(tokens[i])
                i += 1


            # Inferir tipo de la expresión
            tipo_expr = inferir_tipo_expresion(expr_tokens, tipos_vars, ambito)
            if not tipo_compatible(tipo_var, tipo_expr):
                errores.append(f"Error: no se puede asignar tipo '{tipo_expr}' a variable '{nombre_var}' de tipo '{tipo_var}' en ámbito '{ambito}'")
        i += 1
    return errores
def inferir_tipo_expresion(expr_tokens, tipos_vars, ambito):
    tipos = []

    for token, valor in expr_tokens:
        if token == 'id':
            tipo = tipos_vars.get((valor, ambito)) or tipos_vars.get((valor, 'global'))
            tipos.append(tipo)
        elif token == 'num':
            if '.' in valor:
                tipos.append('taolf')
            else:
                tipos.append('tni')
        else:
            tipo = inferir_tipo_literal(valor)
            if tipo:
                tipos.append(tipo)

    tipos_set = set(tipos)

    # Reglas de inferencia de errores
    if 'gnirts' in tipos_set and len(tipos_set) > 1:
        return 'error'
    if 'loob' in tipos_set and ('tni' in tipos_set or 'taolf' in tipos_set or 'gnirts' in tipos_set):
        return 'error'

    # Si hay strings puros
    if tipos_set == {'gnirts'}:
        return 'gnirts'

    # Si hay floats, retorna float
    if 'taolf' in tipos_set:
        return 'taolf'
    if 'tni' in tipos_set:
        return 'tni'
    if 'loob' in tipos_set:
        return 'loob'

    return tipos[0] if tipos else None

def tipo_compatible(tipo_var, tipo_expr):
    if tipo_expr == 'error' or tipo_expr is None:
        return False
    if tipo_var == tipo_expr:
        return True
    if tipo_var == 'tni' and tipo_expr == 'taolf':
        return True  # float a int es tolerable
    if tipo_var == 'taolf' and tipo_expr == 'tni':
        return True
    return False
