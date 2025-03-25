# LENGUAJE SKRN

## INTEGRANTES
- Hugo Alonso Youzzueff Diaz Chavez
- Juan José Huamaní Vásquez
- Melvin Jarred Yabar Carazas
- Gabriel Frank Krisna Zela Flores

## DOCENTE
- Vicente Enrique Machaca Arceda

### Fecha: 20/03/2025

## Nombre del lenguaje propuesto
El lenguaje se llama **SKRN**.

## Justificación y descripción del lenguaje
**SKRN** es un lenguaje de programación diseñado con un enfoque didáctico, pensado para facilitar el aprendizaje de estructuras de control y funciones. Su principal característica es el uso de palabras clave en español y su transliteración al ruso, lo que lo hace único y fácil de entender.

Está inspirado en lenguajes como **Python y C**, manteniendo una estructura clara y modular que permite una programación ordenada y accesible. Su sintaxis intuitiva lo hace ideal para quienes están dando sus primeros pasos en la programación, al tiempo que ofrece herramientas suficientes para desarrollar lógica estructurada de manera efectiva.

## Estructura general del lenguaje
**SKRN** utiliza una sintaxis sencilla basada en palabras clave fácilmente reconocibles. Permite definir funciones, usar condicionales y manejar bucles sin mayor complejidad, favoreciendo un código limpio y legible.

### Principales características:
- Uso de palabras clave en español y ruso transliterado.
- Sintaxis clara y fácil de leer.
- Soporte para estructuras de control como condicionales (`if`), bucles (`while`, `do-while`).
- Capacidad para definir funciones y trabajar con recursividad.
- Declaración de variables con inferencia de tipo implícita, simplificando su uso.

## Tabla de Tokens
| Token   | Expresión regular | Descripción |
|---------|------------------|-------------|
| ID      | `[a-zA-Z][a-zA-Z0-9]*` | Identificadores de variables y funciones. |
| NUM     | `[0-9]+` | Números enteros. |
| ASSIGN  | `=` | Operador de asignación. |
| PLUS    | `+` | Operador de suma. |
| MINUS   | `-` | Operador de resta. |
| TIMES   | `*` | Operador de multiplicación. |
| DIVIDE  | `/` | Operador de división. |
| IF      | `si` | Estructura condicional. |
| THEN    | `entonces` | Palabra clave para el cuerpo del condicional. |
| ENDIF   | `fin_si` | Fin de la estructura `if`. |
| WHILE   | `mientras` | Comienzo de un bucle `while`. |
| DO      | `hacer` | Indica el bloque de código del bucle `while`. |
| ENDWHILE | `fin_mientras` | Fin del bucle `while`. |
| FUNC    | `function` | Palabra clave para definir funciones. |
| CALL    | `llamar` | Palabra clave para invocar funciones. |
| RETURN  | `retornar` | Palabra clave para devolver valores en funciones. |
| LPAREN  | `(` | Paréntesis izquierdo. |
| RPAREN  | `)` | Paréntesis derecho. |
| LBRACE  | `{` | Llave izquierda (para bloques de código). |
| RBRACE  | `}` | Llave derecha (para bloques de código). |
| COMMENT | `#.*` | Comentarios de una sola línea. |

## Tabla de Tokens en Español y Ruso (Transliterado)
| Token en español | Token en ruso (transliterado) |
|------------------|------------------------------|
| ID              | ID |
| NUM            | CHISLO |
| ASSIGN         | PRISVOIT |
| PLUS          | PLYUS |
| MINUS         | MINUS |
| TIMES         | UMNOZHIT |
| DIVIDE        | DELIT |
| IF            | ESLI |
| THEN          | TOGDA |
| ENDIF         | KONETS_ESLI |
| WHILE         | POKA |
| DO            | DELAT |
| ENDWHILE      | KONETS_POKA |
| FUNC          | FUNKTSIYA |
| CALL          | VYZVAT |
| RETURN        | VOZVRAT |
| LPAREN        | `(` |
| RPAREN        | `)` |
| LBRACE        | `{` |
| RBRACE        | `}` |
| COMMENT       | `#` |

## Ejemplos en Lenguaje SKRN
### (1) Hola Mundo
```skrn
funktisiya main() {
    vyzvat "Hola, Mundo!"
    vozvrat
}
```

### (2) Ejemplo con bucles anidados
```skrn
funktisiya main() {
    i = 0
    poka (i < 5) delat {
        j = 0
        poka (j < 5) delat {
            vyzvat i + " " + j
            j = j + 1
        }
        i = i + 1
    }
    vozvrat
}
```

### (3) Ejemplo con recursividad (Factorial)
```skrn
funktisiya factorial(n) {
    esli (n == 0) togda {
        vozvrat 1
    }
    vozvrat n * factorial(n - 1)
}

funktisiya main() {
    rezultat = factorial(5)
    vyzvat rezultat
    vozvrat
}
```

