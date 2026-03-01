def normalizza_nome(nome):
    nome = nome.strip()
    return nome
print(normalizza_nome("  marco rossi  "))      # Output: "Marco Rossi"
print(normalizza_nome("giovanni de LUCA"))    # Output: "Giovanni De Luca"
print(normalizza_nome("  anna-maria lombardi")) # Output: "Anna-Maria Lombardi"