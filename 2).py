def contar_a(string):
    # Contar a quantidade de 'a' e 'A'
    return string.lower().count('a')

# Exemplo de uso:
texto = input("Informe uma string: ")
quantidade = contar_a(texto)
print(f"A letra 'a' aparece {quantidade} vezes na string.")
