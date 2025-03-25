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
| **NUM**     | `[0-9]+` | Números enteros. |
| **ASSIGN**  | `=` | Operador de asignación. |
| **PLUS**    | `+` | Operador de suma. |
| **MINUS**   | `-` | Operador de resta. |
| **TIMES**   | `*` | Operador de multiplicación. |
| **DIVIDE**  | `/` | Operador de división. |
| **IF**      | `si` | Estructura condicional. |
| **THEN**    | `entonces` | Cuerpo del condicional. |
| **ENDIF**   | `fin_si` | Fin del `if`. |
| **WHILE**   | `mientras` | Comienzo de un bucle `while`. |
| **DO**      | `hacer` | Indica el bloque de código. |
| **ENDWHILE** | `fin_mientras` | Fin del bucle `while`. |
| **FUNC**    | `function` | Definir funciones. |
| **CALL**    | `llamar` | Invocar funciones. |
| **RETURN**  | `retornar` | Devolver valores. |
| **LPAREN**  | `(` | Paréntesis izquierdo. |
| **RPAREN**  | `)` | Paréntesis derecho. |
| **LBRACE**  | `{` | Llave izquierda. |
| **RBRACE**  | `}` | Llave derecha. |
| **COMMENT** | `#.*` | Comentarios de una sola línea. |

---

## 🌍 Tabla de Tokens en Español y Ruso (Transliterado)
| Español | Ruso (Transliterado) |
|---------|----------------------|
| **ID**  | ID |
| **NUM** | CHISLO |
| **ASSIGN** | PRISVOIT |
| **PLUS** | PLYUS |
| **MINUS** | MINUS |
| **TIMES** | UMNOZHIT |
| **DIVIDE** | DELIT |
| **IF** | ESLI |
| **THEN** | TOGDA |
| **ENDIF** | KONETS_ESLI |
| **WHILE** | POKA |
| **DO** | DELAT |
| **ENDWHILE** | KONETS_POKA |
| **FUNC** | FUNKTSIYA |
| **CALL** | VYZVAT |
| **RETURN** | VOZVRAT |
| **LPAREN** | `(` |
| **RPAREN** | `)` |
| **LBRACE** | `{` |
| **RBRACE** | `}` |
| **COMMENT** | `#` |

---

## 🔥 Ejemplos en Lenguaje SKRN
### 🖥️ (1) Hola Mundo 🌎
```skrn
funktisiya main() {
    vyzvat "Hola, Mundo!"
    vozvrat
}
```

### 🔄 (2) Bucles anidados 🔄
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

### 🧮 (3) Recursividad (Factorial) 🧮
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

---
🚀 **SKRN: Un lenguaje accesible, didáctico y potente.** 🔥


