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
**SKRN** es un lenguaje de programación con un enfoque **didáctico**, diseñado para facilitar el aprendizaje de estructuras de control y funciones. Su principal característica es el **uso de palabras clave en español y su transliteración al ruso**, lo que lo hace único y fácil de entender.

🔹 Inspirado en **Python y C**.
🔹 Estructura clara y modular.
🔹 Sintaxis intuitiva, ideal para principiantes.
🔹 Herramientas suficientes para desarrollar lógica estructurada.

---

## 📌 Estructura general del lenguaje
**SKRN** utiliza una sintaxis sencilla basada en palabras clave fácilmente reconocibles. Permite definir funciones, usar condicionales y manejar bucles sin mayor complejidad, favoreciendo un código limpio y legible.

### ✨ Principales características:
✔ Uso de palabras clave en **español** y **ruso transliterado**.
✔ **Sintaxis clara** y fácil de leer.
✔ Soporte para **estructuras de control** (`if`, `while`, `do-while`).
✔ Capacidad para **definir funciones** y usar **recursividad**.
✔ **Inferencia de tipos implícita**, simplificando su uso.

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


