def predictive_parser(input_tokens):
    parsing_table = {
        'E': {
            'int': ['T', 'X'],
            '(': ['T', 'X']
        },
        'X': {
            '+': ['+', 'E'],
            ')': [],
            '$': [],
        },
        'T': {
            'int': ['int', 'Y'],
            '(': ['(', 'E', ')']
        },
        'Y': {
            '*': ['*', 'T'],
            '+': [],
            ')': [],
            '$': []
        }
    }

    stack = ['$', 'E']
    input_tokens.append('$')
    pointer = 0

    print(f"{'Stack':<20} {'Input':<20} {'Action'}")
    print("-" * 60)

    while stack:
        top = stack.pop()
        current_input = input_tokens[pointer]

        print(f"{' '.join(stack[::-1]):<20} {' '.join(input_tokens[pointer:]):<20}", end=" ")

        if top == current_input == '$':
            print("ACCEPT")
            break

        elif top in ['int', '+', '*', '(', ')', '$']:  # terminal
            if top == current_input:
                print("terminal")
                pointer += 1
            else:
                print("ERROR: terminal mismatch")
                break

        elif top in parsing_table:
            rule = parsing_table[top].get(current_input)
            if rule is not None:
                if rule:  # Not epsilon
                    stack.extend(reversed(rule))
                    print(f"{' '.join(rule)}")
                else:  # epsilon
                    print("ε")
            else:
                print("ERROR: no rule found")
                break
        else:
            print(f"ERROR: unknown symbol {top}")
            break


# Ejecutar el parser con esta entrada
input_string = ['int', '+', '+', 'int']
predictive_parser(input_string)
