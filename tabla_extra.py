def imprimir_first(first):
    print("\nConjuntos First:")
    for no_terminal, simbolos in sorted(first.items()):
        simbolos_str = ', '.join(sorted(simbolos))
        print(f"First({no_terminal}) = {{{simbolos_str}}}")

def imprimir_follow(follow):
    print("\nConjuntos Follow:")
    for no_terminal, simbolos in sorted(follow.items()):
        simbolos_str = ', '.join(sorted(simbolos))
        print(f"Follow({no_terminal}) = {{{simbolos_str}}}")