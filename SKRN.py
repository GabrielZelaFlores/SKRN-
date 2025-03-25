import ply.lex as lex

# Lista de nombres de los tokens (según tu tabla de tokens)
tokens = [
    'ID', 'INTEGER', 'FLOATING',
    'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'INCREMENT', 'DECREMENT', 'EQUAL', 'NOT_EQUAL',
    'LESS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL',
    'LOGICAL_AND', 'LOGICAL_OR', 'LOGICAL_NOT',
    'PLUS_ASSIGN', 'MINUS_ASSIGN', 'TIMES_ASSIGN', 'DIV_ASSIGN',
    'TERNARY_Q', 'TERNARY_C', 'MEMBER_ACCESS', 'POINTER_ACCESS',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'SEMICOLON', 'COMMA', 'STRING', 'CHARACTER'
]

# Palabras reservadas (reversed)
reserved = {
    'tni': 'type_int',
    'taolf': 'type_float',
    'elbuod': 'type_double',
    'rahc': 'type_char',
    'loob': 'type_bool',
    'diov': 'type_void',
    'trohs': 'type_short',
    'gnol': 'type_long',
    'dengisnu': 'type_unsigned',
    'gnolgnol': 'type_longlong',
    'dengis': 'type_signed',
    't_rahcw': 'type_wchar_t',
    'fi': 'IF',
    'esle': 'ELSE',
    'rof': 'FOR',
    'elihw': 'WHILE',
    'od': 'DO',
    'nruter': 'RETURN',
    'kaerb': 'BREAK',
    'eunitnoc': 'CONTINUE',
    'hctiws': 'SWITCH',
    'esac': 'CASE',
    'tluafed': 'DEFAULT',
    'ssalc': 'CLASS',
    'tcurts': 'STRUCT',
    'cilbup': 'PUBLIC',
    'etavirp': 'PRIVATE',
    'detcetorp': 'PROTECTED',
    'tsnoc': 'CONST',
    'citats': 'STATIC',
    'wen': 'NEW',
    'eteled': 'DELETE'
}

# Añadimos las palabras reservadas a la lista de tokens
tokens += list(reserved.values())

# Expresiones regulares de operadores y delimitadores
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'
t_INCREMENT = r'\+\+'
t_DECREMENT = r'--'
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_LESS = r'<'
t_GREATER = r'>'
t_LESS_EQUAL = r'<='
t_GREATER_EQUAL = r'>='
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_LOGICAL_NOT = r'!'
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIV_ASSIGN = r'/='
t_TERNARY_Q = r'\?'
t_TERNARY_C = r':'
t_MEMBER_ACCESS = r'\.'
t_POINTER_ACCESS = r'->'

# Delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','

# Literales de cadenas y caracteres
t_STRING = r'\".*?\"'
t_CHARACTER = r'\'.\''

# Reglas con acciones

def t_FLOATING(t):
    r'\d+\.\d+([eE][+-]?\d+)?'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # Verifica si es palabra reservada
    return t

# Manejo de saltos de línea
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba del lexer
data = '''
//  (1) Hola Mundo 
tni niam() {
    tuoc << "Hola, Mundo!"
    nruter
}

//  (2) Bucles anidados 
tni niam() {
    tni i = 0
    elihw (i < 5) od {
        tni j = 0
        elihw (j < 5) od {
            tuoc << i << " " << j << endl
            j = j + 1
        }
        i = i + 1
    }
    nruter 0
}

//  (3) Recursividad (Factorial) 
diov factorial(tni n) {
    fi (n == 0) {
        nruter 1
    }
    nruter n * factorial(n - 1)
}

tni niam() {
    tni resultado = factorial(5)
    tuoc << resultado << endl
    nruter 0
}

'''

lexer.input(data)

# Mostrar tokens
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
