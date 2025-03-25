# 📌 LENGUAJE SKRN

## 👨‍💻 INTEGRANTES
- **Hugo Alonso Youzzueff Diaz Chavez**
- **Juan José Huamaní Vásquez**
- **Melvin Jarred Yabar Carazas**
- **Gabriel Frank Krisna Zela Flores**

## 🎓 DOCENTE
- **Vicente Enrique Machaca Arceda**

📅 **Fecha:** *20/03/2025*

---

## 🚀 Nombre del lenguaje propuesto
El lenguaje se llama **SKRN**.

## 🎯 Justificación y descripción del lenguaje
**SKRN** un lenguaje de programación diseñado especialmente para facilitar el aprendizaje de conceptos fundamentales en programación. Lo que distingue a SKRN es su uso innovador de palabras clave en español escritas al revés, lo que ayuda a los principiantes a relacionar fácilmente los comandos con su significado original.

🔹 Inspirado en Python y C para combinar facilidad de uso con control eficiente de recursos.
🔹 Estructura clara y modular que favorece la reutilización del código.
🔹 Uso de palabras clave en español invertidas, lo que facilita su reconocimiento.

---

## 📌 Estructura general del lenguaje
El lenguaje **SKRN** se basa en una sintaxis simplificada que mantiene las estructuras fundamentales de la programación imperativa.

Ejemplo de código en SKRN:

```skrn
fi (x > 0) {
    nruter x;
} esle {
    nruter -x;
}
```

📌 En este código, el condicional fi evalúa si x es mayor que 0. Si se cumple, se retorna x; de lo contrario (esle), se retorna -x.

Las estructuras de control básicas incluyen:
✔ Condicionales: fi, esle
✔ Bucles: rof, elihw, od-elihw
✔ Definición de funciones con nruter
✔ Manejo de estructuras y clases con ssalc y tcurts

---

✨ Principales características
✔ Uso de palabras clave en español invertidas para facilitar la asociación con conceptos conocidos.
✔ Soporte para estructuras de control (fi, esle, rof, elihw).
✔ Capacidad de definir funciones y usar recursividad mediante nruter.
✔ Inferencia de tipos implícita, reduciendo la necesidad de declaraciones manuales.
✔ Operadores y sintaxis similares a C y Python, lo que permite una transición sencilla a otros lenguajes.
✔ Manejo de clases y estructuras, facilitando la programación orientada a objetos.

---

## 🔢 Tabla de Tokens
| Token   | Expresión regular | Descripción |
|---------|------------------|-------------|
| **ID**      | `[a-zA-Z][a-zA-Z0-9]*` | Identificadores de variables y funciones. |
| **INTEGER**     | `[0-9]+` | Números enteros. |
| **FLOATING**     | `[0-9]+\.[0-9]+([eE][+-]?[0-9]+)?` | Números reales. |
| **ASSIGN**             | `=`         | Operador de asignación.                             |
| **PLUS**               | `+`         | Operador de suma.                                   |
| **MINUS**              | `-`         | Operador de resta.                                  |
| **TIMES**              | `*`         | Operador de multiplicación.                         |
| **DIVIDE**             | `/`         | Operador de división.                               |
| **MODULO**             | `%`         | Operador de módulo (residuo de división).           |
| **INCREMENT**          | `++`        | Operador de incremento.                             |
| **DECREMENT**          | `--`        | Operador de decremento.                             |
| **EQUAL**              | `==`        | Operador de comparación de igualdad.                |
| **NOT_EQUAL**          | `!=`        | Operador de comparación de desigualdad.             |
| **LESS**               | `<`         | Operador de menor que.                              |
| **GREATER**            | `>`         | Operador de mayor que.                              |
| **LESS_EQUAL**         | `<=`        | Operador de menor o igual que.                      |
| **GREATER_EQUAL**      | `>=`        | Operador de mayor o igual que.                      |
| **LOGICAL_AND**        | `&&`        | Operador lógico AND.                                |
| **LOGICAL_OR**         | `ll`        | Operador lógico OR.                                 |
| **LOGICAL_NOT**        | `!`         | Operador lógico NOT (negación).                     |
| **PLUS_ASSIGN**        | `+=`        | Operador de asignación con suma.                    |
| **MINUS_ASSIGN**       | `-=`        | Operador de asignación con resta.                   |
| **TIMES_ASSIGN**       | `*=`        | Operador de asignación con multiplicación.          |
| **DIV_ASSIGN**         | `/=`        | Operador de asignación con división.                |
| **TERNARY_Q**          | `?`         | Operador ternario (condición - signo de pregunta).  |
| **TERNARY_C**          | `:`         | Operador ternario (condición - dos puntos).         |
| **MEMBER_ACCESS**      | `.`         | Operador de acceso a miembros.                      |
| **POINTER_ACCESS**     | `->`        | Operador de acceso a miembros mediante puntero.     |
| **LPAREN**    | `\(`         | Paréntesis izquierdo.                      |
| **RPAREN**    | `\)`         | Paréntesis derecho.                       |
| **LBRACE**    | `{`          | Llave izquierda.                         |
| **RBRACE**    | `}`          | Llave derecha.                           |
| **LBRACKET**  | `\[`         | Corchete izquierdo.                      |
| **RBRACKET**  | `\]`         | Corchete derecho.                        |
| **SEMICOLON** | `;`          | Fin de instrucción.                      |
| **COMMA**     | `,`          | Separador de elementos.                  |
| **type_int**       | `tni`         | Tipo de dato entero.                                    |
| **type_float**     | `taolf`       | Número de punto flotante de precisión simple.            |
| **type_double**    | `elbuod`      | Número de punto flotante de doble precisión.             |
| **type_char**      | `rahc`        | Carácter individual.                                     |
| **type_bool**      | `loob`        | Tipo booleano (verdadero o falso).                       |
| **type_void**      | `diov`        | No retorna ningún valor (tipo vacío).                    |
| **type_short**     | `trohs`       | Entero corto (menor rango que `int`).                    |
| **type_long**      | `gnol`        | Entero largo (mayor rango que `int`).                    |
| **type_unsigned**  | `dengisnu`    | Entero sin signo (solo valores positivos).               |
| **type_longlong**  | `gnolgnol`    | Entero de rango extendido (mayor que `long`).            |
| **type_signed**    | `dengis`      | Especifica que un entero puede ser negativo o positivo.  |
| **type_wchar_t**   | `t_rahcw`     | Tipo para caracteres anchos (soporte de Unicode).        |
| **IF**        | `fi`        | Estructura condicional.                        |
| **ELSE**      | `esle`      | Alternativa en la estructura condicional.      |
| **FOR**       | `rof`       | Comienzo de un bucle `for`.                    |
| **WHILE**     | `elihw`     | Comienzo de un bucle `while`.                  |
| **DO**        | `od`        | Inicio de un bloque en un ciclo `do-while`.    |
| **RETURN**    | `nruter`    | Retornar un valor de una función.              |
| **BREAK**     | `kaerb`     | Salir de un ciclo o `switch`.                  |
| **CONTINUE**  | `eunitnoc`  | Saltar a la siguiente iteración del ciclo.     |
| **SWITCH**    | `hctiws`    | Selección múltiple de casos.                   |
| **CASE**      | `esac`      | Caso dentro de un `switch`.                    |
| **DEFAULT**   | `tluafed`   | Caso por defecto en un `switch`.               |
| **CLASS**     | `ssalc`     | Definición de una clase.                       |
| **STRUCT**    | `tcurts`    | Definición de una estructura.                  |
| **PUBLIC**    | `cilbup`    | Acceso público en una clase.                   |
| **PRIVATE**   | `etavirp`   | Acceso privado en una clase.                   |
| **PROTECTED** | `detcetorp` | Acceso protegido en una clase.                 |
| **CONST**     | `tsnoc`     | Declaración de una constante.                  |
| **STATIC**    | `citats`    | Declaración de un miembro estático.            |
| **NEW**       | `wen`       | Reserva dinámica de memoria.                  |
| **DELETE**    | `eteled`    | Libera memoria dinámica.                      |

---

## 🔥 Ejemplos en Lenguaje SKRN
### 🖥️ (1) Hola Mundo 🌎
```skrn
tni niam() {
    tuoc << "Hola, Mundo!"
    nruter
}
```

### 🔄 (2) Bucles anidados 🔄
```skrn
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
```

### 🧮 (3) Recursividad (Factorial) 🧮
```skrn
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
```

---
🚀 **SKRN: Un lenguaje accesible, didáctico y potente.** 🔥


